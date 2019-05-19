# -*- coding: utf-8 -*-
"""
Models for Student Identity Verification

This is where we put any models relating to establishing the real-life identity
of a student over a period of time. Right now, the only models are the abstract
`PhotoVerification`, and its one concrete implementation
`SoftwareSecurePhotoVerification`. The hope is to keep as much of the
photo verification process as generic as possible.
"""
import functools
import json
import logging
import os.path
import uuid
from datetime import datetime, timedelta
from email.utils import formatdate

import pytz
import requests
import six
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.urls import reverse
from django.db import models
from django.dispatch import receiver
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel
from opaque_keys.edx.django.models import CourseKeyField

from lms.djangoapps.verify_student.ssencrypt import (
    encrypt_and_encode,
    generate_signed_message,
    random_aes_key,
    rsa_encrypt
)
from openedx.core.djangoapps.signals.signals import LEARNER_NOW_VERIFIED
from openedx.core.storage import get_storage

from .utils import earliest_allowed_verification_date

log = logging.getLogger(__name__)


def generateUUID():  # pylint: disable=invalid-name
    """ Utility function; generates UUIDs """
    return str(uuid.uuid4())


class VerificationException(Exception):
    pass


def status_before_must_be(*valid_start_statuses):
    """
    Helper decorator with arguments to make sure that an object with a `status`
    attribute is in one of a list of acceptable status states before a method
    is called. You could use it in a class definition like:

        @status_before_must_be("submitted", "approved", "denied")
        def refund_user(self, user_id):
            # Do logic here...

    If the object has a status that is not listed when the `refund_user` method
    is invoked, it will throw a `VerificationException`. This is just to avoid
    distracting boilerplate when looking at a Model that needs to go through a
    workflow process.
    """
    def decorator_func(func):
        """
        Decorator function that gets returned
        """
        @functools.wraps(func)
        def with_status_check(obj, *args, **kwargs):
            if obj.status not in valid_start_statuses:
                exception_msg = (
                    u"Error calling {} {}: status is '{}', must be one of: {}"
                ).format(func, obj, obj.status, valid_start_statuses)
                raise VerificationException(exception_msg)
            return func(obj, *args, **kwargs)

        return with_status_check

    return decorator_func


class IDVerificationAttempt(StatusModel):
    """
    Each IDVerificationAttempt represents a Student's attempt to establish
    their identity through one of several methods that inherit from this Model,
    including PhotoVerification and SSOVerification.

    .. pii: The User's name is stored in this and sub-models
    .. pii_types: name
    .. pii_retirement: retained
    """
    STATUS = Choices('created', 'ready', 'submitted', 'must_retry', 'approved', 'denied')
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)

    # They can change their name later on, so we want to copy the value here so
    # we always preserve what it was at the time they requested. We only copy
    # this value during the mark_ready() step. Prior to that, you should be
    # displaying the user's name from their user.profile.name.
    name = models.CharField(blank=True, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta(object):
        app_label = "verify_student"
        abstract = True
        ordering = ['-created_at']

    @property
    def expiration_datetime(self):
        """Datetime that the verification will expire. """
        days_good_for = settings.VERIFY_STUDENT["DAYS_GOOD_FOR"]
        return self.created_at + timedelta(days=days_good_for)

    def should_display_status_to_user(self):
        """Whether or not the status from this attempt should be displayed to the user."""
        raise NotImplementedError

    def active_at_datetime(self, deadline):
        """Check whether the verification was active at a particular datetime.

        Arguments:
            deadline (datetime): The date at which the verification was active
                (created before and expiration datetime is after today).

        Returns:
            bool

        """
        return (
            self.created_at < deadline and
            self.expiration_datetime > datetime.now(pytz.UTC)
        )


class ManualVerification(IDVerificationAttempt):
    """
    Each ManualVerification represents a user's verification that bypasses the need for
    any other verification.

    .. pii: The User's name is stored in the parent model
    .. pii_types: name
    .. pii_retirement: retained
    """

    reason = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            'Specifies the reason for manual verification of the user.'
        )
    )

    class Meta(object):
        app_label = 'verify_student'

    def __unicode__(self):
        return 'ManualIDVerification for {name}, status: {status}'.format(
            name=self.name,
            status=self.status,
        )

    def should_display_status_to_user(self):
        """
        Whether or not the status should be displayed to the user.
        """
        return False


class SSOVerification(IDVerificationAttempt):
    """
    Each SSOVerification represents a Student's attempt to establish their identity
    by signing in with SSO. ID verification through SSO bypasses the need for
    photo verification.

    .. no_pii:
    """

    OAUTH2 = 'third_party_auth.models.OAuth2ProviderConfig'
    SAML = 'third_party_auth.models.SAMLProviderConfig'
    LTI = 'third_party_auth.models.LTIProviderConfig'
    IDENTITY_PROVIDER_TYPE_CHOICES = (
        (OAUTH2, 'OAuth2 Provider'),
        (SAML, 'SAML Provider'),
        (LTI, 'LTI Provider'),
    )

    identity_provider_type = models.CharField(
        max_length=100,
        blank=False,
        choices=IDENTITY_PROVIDER_TYPE_CHOICES,
        default=SAML,
        help_text=(
            'Specifies which type of Identity Provider this verification originated from.'
        )
    )

    identity_provider_slug = models.SlugField(
        max_length=30, db_index=True, default='default',
        help_text=(
            'The slug uniquely identifying the Identity Provider this verification originated from.'
        ))

    class Meta(object):
        app_label = "verify_student"

    def __unicode__(self):
        return 'SSOIDVerification for {name}, status: {status}'.format(
            name=self.name,
            status=self.status,
        )

    def should_display_status_to_user(self):
        """Whether or not the status from this attempt should be displayed to the user."""
        return False


class PhotoVerification(IDVerificationAttempt):
    """
    Each PhotoVerification represents a Student's attempt to establish
    their identity by uploading a photo of themselves and a picture ID. An
    attempt actually has a number of fields that need to be filled out at
    different steps of the approval process. While it's useful as a Django Model
    for the querying facilities, **you should only edit a `PhotoVerification`
    object through the methods provided**. Initialize them with a user:

    attempt = PhotoVerification(user=user)

    We track this attempt through various states:

    `created`
        Initial creation and state we're in after uploading the images.
    `ready`
        The user has uploaded their images and checked that they can read the
        images. There's a separate state here because it may be the case that we
        don't actually submit this attempt for review until payment is made.
    `submitted`
        Submitted for review. The review may be done by a staff member or an
        external service. The user cannot make changes once in this state.
    `must_retry`
        We submitted this, but there was an error on submission (i.e. we did not
        get a 200 when we POSTed to Software Secure)
    `approved`
        An admin or an external service has confirmed that the user's photo and
        photo ID match up, and that the photo ID's name matches the user's.
    `denied`
        The request has been denied. See `error_msg` for details on why. An
        admin might later override this and change to `approved`, but the
        student cannot re-open this attempt -- they have to create another
        attempt and submit it instead.

    Because this Model inherits from IDVerificationAttempt, which inherits
    from StatusModel, we can also do things like:

        attempt.status == PhotoVerification.STATUS.created
        attempt.status == "created"
        pending_requests = PhotoVerification.submitted.all()

    .. pii: The User's name is stored in the parent model, this one stores links to face and photo ID images
    .. pii_types: name, image
    .. pii_retirement: retained
    """
    ######################## Fields Set During Creation ########################
    # See class docstring for description of status states
    # Where we place the uploaded image files (e.g. S3 URLs)
    face_image_url = models.URLField(blank=True, max_length=255)
    photo_id_image_url = models.URLField(blank=True, max_length=255)

    # Randomly generated UUID so that external services can post back the
    # results of checking a user's photo submission without use exposing actual
    # user IDs or something too easily guessable.
    receipt_id = models.CharField(
        db_index=True,
        default=generateUUID,
        max_length=255,
    )

    # Indicates whether or not a user wants to see the verification status
    # displayed on their dash.  Right now, only relevant for allowing students
    # to "dismiss" a failed midcourse reverification message
    # TODO: This field is deprecated.
    display = models.BooleanField(db_index=True, default=True)

    ######################## Fields Set When Submitting ########################
    submitted_at = models.DateTimeField(null=True, db_index=True)

    #################### Fields Set During Approval/Denial #####################
    # If the review was done by an internal staff member, mark who it was.
    reviewing_user = models.ForeignKey(
        User,
        db_index=True,
        default=None,
        null=True,
        related_name="photo_verifications_reviewed",
        on_delete=models.CASCADE,
    )

    # Mark the name of the service used to evaluate this attempt (e.g
    # Software Secure).
    reviewing_service = models.CharField(blank=True, max_length=255)

    # If status is "denied", this should contain text explaining why.
    error_msg = models.TextField(blank=True)

    # Non-required field. External services can add any arbitrary codes as time
    # goes on. We don't try to define an exhuastive list -- this is just
    # capturing it so that we can later query for the common problems.
    error_code = models.CharField(blank=True, max_length=50)

    class Meta(object):
        app_label = "verify_student"
        abstract = True
        ordering = ['-created_at']

    def parsed_error_msg(self):
        """
        Sometimes, the error message we've received needs to be parsed into
        something more human readable

        The default behavior is to return the current error message as is.
        """
        return self.error_msg

    @status_before_must_be("created")
    def upload_face_image(self, img):
        raise NotImplementedError

    @status_before_must_be("created")
    def upload_photo_id_image(self, img):
        raise NotImplementedError

    @status_before_must_be("created")
    def mark_ready(self):
        """
        Mark that the user data in this attempt is correct. In order to
        succeed, the user must have uploaded the necessary images
        (`face_image_url`, `photo_id_image_url`). This method will also copy
        their name from their user profile. Prior to marking it ready, we read
        this value directly from their profile, since they're free to change it.
        This often happens because people put in less formal versions of their
        name on signup, but realize they want something different to go on a
        formal document.

        Valid attempt statuses when calling this method:
            `created`

        Status after method completes: `ready`

        Other fields that will be set by this method:
            `name`

        State Transitions:

        `created` → `ready`
            This is what happens when the user confirms to us that the pictures
            they uploaded are good. Note that we don't actually do a submission
            anywhere yet.
        """
        # At any point prior to this, they can change their names via their
        # student dashboard. But at this point, we lock the value into the
        # attempt.
        self.name = self.user.profile.name
        self.status = "ready"
        self.save()

    @status_before_must_be("must_retry", "submitted", "approved", "denied")
    def approve(self, user_id=None, service=""):
        """
        Approve this attempt. `user_id`

        Valid attempt statuses when calling this method:
            `submitted`, `approved`, `denied`

        Status after method completes: `approved`

        Other fields that will be set by this method:
            `reviewed_by_user_id`, `reviewed_by_service`, `error_msg`

        State Transitions:

        `submitted` → `approved`
            This is the usual flow, whether initiated by a staff user or an
            external validation service.
        `approved` → `approved`
            No-op. First one to approve it wins.
        `denied` → `approved`
            This might happen if a staff member wants to override a decision
            made by an external service or another staff member (say, in
            response to a support request). In this case, the previous values
            of `reviewed_by_user_id` and `reviewed_by_service` will be changed
            to whoever is doing the approving, and `error_msg` will be reset.
            The only record that this record was ever denied would be in our
            logs. This should be a relatively rare occurence.
        """
        # If someone approves an outdated version of this, the first one wins
        if self.status == "approved":
            return

        log.info(u"Verification for user '{user_id}' approved by '{reviewer}'.".format(
            user_id=self.user, reviewer=user_id
        ))
        self.error_msg = ""  # reset, in case this attempt was denied before
        self.error_code = ""  # reset, in case this attempt was denied before
        self.reviewing_user = user_id
        self.reviewing_service = service
        self.status = "approved"
        self.save()
        # Emit signal to find and generate eligible certificates
        LEARNER_NOW_VERIFIED.send_robust(
            sender=PhotoVerification,
            user=self.user
        )

    @status_before_must_be("must_retry", "submitted", "approved", "denied")
    def deny(self,
             error_msg,
             error_code="",
             reviewing_user=None,
             reviewing_service=""):
        """
        Deny this attempt.

        Valid attempt statuses when calling this method:
            `submitted`, `approved`, `denied`

        Status after method completes: `denied`

        Other fields that will be set by this method:
            `reviewed_by_user_id`, `reviewed_by_service`, `error_msg`,
            `error_code`

        State Transitions:

        `submitted` → `denied`
            This is the usual flow, whether initiated by a staff user or an
            external validation service.
        `approved` → `denied`
            This might happen if a staff member wants to override a decision
            made by an external service or another staff member, or just correct
            a mistake made during the approval process. In this case, the
            previous values of `reviewed_by_user_id` and `reviewed_by_service`
            will be changed to whoever is doing the denying. The only record
            that this record was ever approved would be in our logs. This should
            be a relatively rare occurence.
        `denied` → `denied`
            Update the error message and reviewing_user/reviewing_service. Just
            lets you amend the error message in case there were additional
            details to be made.
        """
        log.info(u"Verification for user '{user_id}' denied by '{reviewer}'.".format(
            user_id=self.user, reviewer=reviewing_user
        ))
        self.error_msg = error_msg
        self.error_code = error_code
        self.reviewing_user = reviewing_user
        self.reviewing_service = reviewing_service
        self.status = "denied"
        self.save()

    @status_before_must_be("must_retry", "submitted", "approved", "denied")
    def system_error(self,
                     error_msg,
                     error_code="",
                     reviewing_user=None,
                     reviewing_service=""):
        """
        Mark that this attempt could not be completed because of a system error.
        Status should be moved to `must_retry`. For example, if Software Secure
        reported to us that they couldn't process our submission because they
        couldn't decrypt the image we sent.
        """
        if self.status in ["approved", "denied"]:
            return  # If we were already approved or denied, just leave it.

        self.error_msg = error_msg
        self.error_code = error_code
        self.reviewing_user = reviewing_user
        self.reviewing_service = reviewing_service
        self.status = "must_retry"
        self.save()

    @classmethod
    def retire_user(cls, user_id):
        """
        Retire user as part of GDPR Phase I
        Returns 'True' if records found

        :param user_id: int
        :return: bool
        """
        try:
            user_obj = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return False

        photo_objects = cls.objects.filter(
            user=user_obj
        ).update(
            name='',
            face_image_url='',
            photo_id_image_url='',
            photo_id_key=''
        )
        return photo_objects > 0


class SoftwareSecurePhotoVerification(PhotoVerification):
    """
    Model to verify identity using a service provided by Software Secure. Much
    of the logic is inherited from `PhotoVerification`, but this class
    encrypts the photos.

    Software Secure (http://www.softwaresecure.com/) is a remote proctoring
    service that also does identity verification. A student uses their webcam
    to upload two images: one of their face, one of a photo ID. Due to the
    sensitive nature of the data, the following security precautions are taken:

    1. The snapshot of their face is encrypted using AES-256 in CBC mode. All
       face photos are encypted with the same key, and this key is known to
       both Software Secure and edx-platform.

    2. The snapshot of a user's photo ID is also encrypted using AES-256, but
       the key is randomly generated using os.urandom. Every verification
       attempt has a new key. The AES key is then encrypted using a public key
       provided by Software Secure. We store only the RSA-encryped AES key.
       Since edx-platform does not have Software Secure's private RSA key, it
       means that we can no longer even read photo ID.

    3. The encrypted photos are base64 encoded and stored in an S3 bucket that
       edx-platform does not have read access to.

    Note: this model handles *inital* verifications (which you must perform
    at the time you register for a verified cert).

    .. pii: The User's name is stored in the parent model, this one stores links to face and photo ID images
    .. pii_types: name, image
    .. pii_retirement: retained
    """
    # This is a base64.urlsafe_encode(rsa_encrypt(photo_id_aes_key), ss_pub_key)
    # So first we generate a random AES-256 key to encrypt our photo ID with.
    # Then we RSA encrypt it with Software Secure's public key. Then we base64
    # encode that. The result is saved here. Actual expected length is 344.
    photo_id_key = models.TextField(max_length=1024)

    IMAGE_LINK_DURATION = 5 * 60 * 60 * 24  # 5 days in seconds
    copy_id_photo_from = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    # Fields for functionality of sending email when verification expires
    # expiry_date: The date when the SoftwareSecurePhotoVerification will expire
    # expiry_email_date: This field is used to maintain a check for learners to which email
    # to notify for expired verification is already sent.
    expiry_date = models.DateTimeField(null=True, blank=True, db_index=True)
    expiry_email_date = models.DateTimeField(null=True, blank=True, db_index=True)

    @classmethod
    def get_initial_verification(cls, user, earliest_allowed_date=None):
        """Get initial verification for a user with the 'photo_id_key'.

        Arguments:
            user(User): user object
            earliest_allowed_date(datetime): override expiration date for initial verification

        Return:
            SoftwareSecurePhotoVerification (object) or None
        """
        init_verification = cls.objects.filter(
            user=user,
            status__in=["submitted", "approved"],
            created_at__gte=(
                earliest_allowed_date or earliest_allowed_verification_date()
            )
        ).exclude(photo_id_key='')

        return init_verification.latest('created_at') if init_verification.exists() else None

    @status_before_must_be("created")
    def upload_face_image(self, img_data):
        """
        Upload an image of the user's face. `img_data` should be a raw
        bytestream of a PNG image. This method will take the data, encrypt it
        using our FACE_IMAGE_AES_KEY, encode it with base64 and save it to the
        storage backend.

        Yes, encoding it to base64 adds compute and disk usage without much real
        benefit, but that's what the other end of this API is expecting to get.
        """
        # Skip this whole thing if we're running acceptance tests or if we're
        # developing and aren't interested in working on student identity
        # verification functionality. If you do want to work on it, you have to
        # explicitly enable these in your private settings.
        if settings.FEATURES.get('AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING'):
            return

        aes_key_str = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["FACE_IMAGE_AES_KEY"]
        aes_key = aes_key_str.decode("hex")

        path = self._get_path("face")
        buff = ContentFile(encrypt_and_encode(img_data, aes_key))
        self._storage.save(path, buff)

    @status_before_must_be("created")
    def upload_photo_id_image(self, img_data):
        """
        Upload an the user's photo ID image. `img_data` should be a raw
        bytestream of a PNG image. This method will take the data, encrypt it
        using a randomly generated AES key, encode it with base64 and save it
        to the storage backend. The random key is also encrypted using Software
        Secure's public RSA key and stored in our `photo_id_key` field.

        Yes, encoding it to base64 adds compute and disk usage without much real
        benefit, but that's what the other end of this API is expecting to get.
        """
        # Skip this whole thing if we're running acceptance tests or if we're
        # developing and aren't interested in working on student identity
        # verification functionality. If you do want to work on it, you have to
        # explicitly enable these in your private settings.
        if settings.FEATURES.get('AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING'):
            # fake photo id key is set only for initial verification
            self.photo_id_key = 'fake-photo-id-key'
            self.save()
            return

        aes_key = random_aes_key()
        rsa_key_str = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["RSA_PUBLIC_KEY"]
        rsa_encrypted_aes_key = rsa_encrypt(aes_key, rsa_key_str)

        # Save this to the storage backend
        path = self._get_path("photo_id")
        buff = ContentFile(encrypt_and_encode(img_data, aes_key))
        self._storage.save(path, buff)

        # Update our record fields
        self.photo_id_key = rsa_encrypted_aes_key.encode('base64')
        self.save()

    @status_before_must_be("must_retry", "ready", "submitted")
    def submit(self, copy_id_photo_from=None):
        """
        Submit our verification attempt to Software Secure for validation. This
        will set our status to "submitted" if the post is successful, and
        "must_retry" if the post fails.

        Keyword Arguments:
            copy_id_photo_from (SoftwareSecurePhotoVerification): If provided, re-send the ID photo
                data from this attempt.  This is used for reverification, in which new face photos
                are sent with previously-submitted ID photos.

        """
        try:
            response = self.send_request(copy_id_photo_from=copy_id_photo_from)
            if response.ok:
                self.submitted_at = datetime.now(pytz.UTC)
                self.status = "submitted"
                self.save()
            else:
                self.status = "must_retry"
                self.error_msg = response.text
                self.save()
        except Exception:       # pylint: disable=broad-except
            log.exception(
                u'Software Secure submission failed for user %s, setting status to must_retry',
                self.user.username
            )
            self.status = "must_retry"
            self.save()

    def parsed_error_msg(self):
        """
        Parse the error messages we receive from SoftwareSecure

        Error messages are written in the form:

            `[{"photoIdReasons": ["Not provided"]}]`

        Returns:
            str[]: List of error messages.
        """
        parsed_errors = []
        error_map = {
            'EdX name not provided': 'name_mismatch',
            'Name mismatch': 'name_mismatch',
            'Photo/ID Photo mismatch': 'photos_mismatched',
            'ID name not provided': 'id_image_missing_name',
            'Invalid Id': 'id_invalid',
            'No text': 'id_invalid',
            'Not provided': 'id_image_missing',
            'Photo hidden/No photo': 'id_image_not_clear',
            'Text not clear': 'id_image_not_clear',
            'Face out of view': 'user_image_not_clear',
            'Image not clear': 'user_image_not_clear',
            'Photo not provided': 'user_image_missing',
        }

        try:
            messages = set()
            message_groups = json.loads(self.error_msg)

            for message_group in message_groups:
                messages = messages.union(set(*six.itervalues(message_group)))

            for message in messages:
                parsed_error = error_map.get(message)

                if parsed_error:
                    parsed_errors.append(parsed_error)
                else:
                    log.debug(u'Ignoring photo verification error message: %s', message)
        except Exception:   # pylint: disable=broad-except
            log.exception(u'Failed to parse error message for SoftwareSecurePhotoVerification %d', self.pk)

        return parsed_errors

    def image_url(self, name, override_receipt_id=None):
        """
        We dynamically generate this, since we want it the expiration clock to
        start when the message is created, not when the record is created.

        Arguments:
            name (str): Name of the image (e.g. "photo_id" or "face")

        Keyword Arguments:
            override_receipt_id (str): If provided, use this receipt ID instead
                of the ID for this attempt.  This is useful for reverification
                where we need to construct a URL to a previously-submitted
                photo ID image.

        Returns:
            string: The expiring URL for the image.

        """
        path = self._get_path(name, override_receipt_id=override_receipt_id)
        return self._storage.url(path)

    @cached_property
    def _storage(self):
        """
        Return the configured django storage backend.
        """
        config = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]

        # Default to the S3 backend for backward compatibility
        storage_class = config.get("STORAGE_CLASS", "storages.backends.s3boto.S3BotoStorage")
        storage_kwargs = config.get("STORAGE_KWARGS", {})

        # Map old settings to the parameters expected by the storage backend
        if "AWS_ACCESS_KEY" in config:
            storage_kwargs["access_key"] = config["AWS_ACCESS_KEY"]
        if "AWS_SECRET_KEY" in config:
            storage_kwargs["secret_key"] = config["AWS_SECRET_KEY"]
        if "S3_BUCKET" in config:
            storage_kwargs["bucket"] = config["S3_BUCKET"]
            storage_kwargs["querystring_expire"] = self.IMAGE_LINK_DURATION

        return get_storage(storage_class, **storage_kwargs)

    def _get_path(self, prefix, override_receipt_id=None):
        """
        Returns the path to a resource with this instance's `receipt_id`.

        If `override_receipt_id` is given, the path to that resource will be
        retrieved instead. This allows us to retrieve images submitted in
        previous attempts (used for reverification, where we send a new face
        photo with the same photo ID from a previous attempt).
        """
        receipt_id = self.receipt_id if override_receipt_id is None else override_receipt_id
        return os.path.join(prefix, receipt_id)

    def _encrypted_user_photo_key_str(self):
        """
        Software Secure needs to have both UserPhoto and PhotoID decrypted in
        the same manner. So even though this is going to be the same for every
        request, we're also using RSA encryption to encrypt the AES key for
        faces.
        """
        face_aes_key_str = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["FACE_IMAGE_AES_KEY"]
        face_aes_key = face_aes_key_str.decode("hex")
        rsa_key_str = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["RSA_PUBLIC_KEY"]
        rsa_encrypted_face_aes_key = rsa_encrypt(face_aes_key, rsa_key_str)

        return rsa_encrypted_face_aes_key.encode("base64")

    def create_request(self, copy_id_photo_from=None):
        """
        Construct the HTTP request to the photo verification service.

        Keyword Arguments:
            copy_id_photo_from (SoftwareSecurePhotoVerification): If provided, re-send the ID photo
                data from this attempt.  This is used for reverification, in which new face photos
                are sent with previously-submitted ID photos.

        Returns:
            tuple of (header, body), where both `header` and `body` are dictionaries.

        """
        access_key = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["API_ACCESS_KEY"]
        secret_key = settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["API_SECRET_KEY"]

        scheme = "https" if settings.HTTPS == "on" else "http"
        callback_url = "{}://{}{}".format(
            scheme, settings.SITE_NAME, reverse('verify_student_results_callback')
        )

        # If we're copying the photo ID image from a previous verification attempt,
        # then we need to send the old image data with the correct image key.
        photo_id_url = (
            self.image_url("photo_id")
            if copy_id_photo_from is None
            else self.image_url("photo_id", override_receipt_id=copy_id_photo_from.receipt_id)
        )

        photo_id_key = (
            self.photo_id_key
            if copy_id_photo_from is None else
            copy_id_photo_from.photo_id_key
        )

        body = {
            "EdX-ID": str(self.receipt_id),
            "ExpectedName": self.name,
            "PhotoID": photo_id_url,
            "PhotoIDKey": photo_id_key,
            "SendResponseTo": callback_url,
            "UserPhoto": self.image_url("face"),
            "UserPhotoKey": self._encrypted_user_photo_key_str(),
        }
        headers = {
            "Content-Type": "application/json",
            "Date": formatdate(timeval=None, localtime=False, usegmt=True)
        }
        _message, _sig, authorization = generate_signed_message(
            "POST", headers, body, access_key, secret_key
        )
        headers['Authorization'] = authorization

        return headers, body

    def request_message_txt(self):
        """
        This is the body of the request we send across. This is never actually
        used in the code, but exists for debugging purposes -- you can call
        `print attempt.request_message_txt()` on the console and get a readable
        rendering of the request that would be sent across, without actually
        sending anything.
        """
        headers, body = self.create_request()

        header_txt = "\n".join(
            u"{}: {}".format(h, v) for h, v in sorted(headers.items())
        )
        body_txt = json.dumps(body, indent=2, sort_keys=True, ensure_ascii=False).encode('utf-8')

        return header_txt + "\n\n" + body_txt

    def send_request(self, copy_id_photo_from=None):
        """
        Assembles a submission to Software Secure and sends it via HTTPS.

        Keyword Arguments:
            copy_id_photo_from (SoftwareSecurePhotoVerification): If provided, re-send the ID photo
                data from this attempt.  This is used for reverification, in which new face photos
                are sent with previously-submitted ID photos.

        Returns:
            request.Response

        """
        # If AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING is True, we want to
        # skip posting anything to Software Secure. We actually don't even
        # create the message because that would require encryption and message
        # signing that rely on settings.VERIFY_STUDENT values that aren't set
        # in dev. So we just pretend like we successfully posted
        if settings.FEATURES.get('AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING'):
            fake_response = requests.Response()
            fake_response.status_code = 200
            return fake_response

        headers, body = self.create_request(copy_id_photo_from=copy_id_photo_from)
        response = requests.post(
            settings.VERIFY_STUDENT["SOFTWARE_SECURE"]["API_URL"],
            headers=headers,
            data=json.dumps(body, indent=2, sort_keys=True, ensure_ascii=False).encode('utf-8'),
            verify=False
        )

        log.info(u"Sent request to Software Secure for receipt ID %s.", self.receipt_id)
        if copy_id_photo_from is not None:
            log.info(
                (
                    u"Software Secure attempt with receipt ID %s used the same photo ID "
                    u"data as the receipt with ID %s"
                ),
                self.receipt_id, copy_id_photo_from.receipt_id
            )

        log.debug("Headers:\n{}\n\n".format(headers))
        log.debug("Body:\n{}\n\n".format(body))
        log.debug(u"Return code: {}".format(response.status_code))
        log.debug(u"Return message:\n\n{}\n\n".format(response.text))

        return response

    def should_display_status_to_user(self):
        """Whether or not the status from this attempt should be displayed to the user."""
        return True


class VerificationDeadline(TimeStampedModel):
    """
    Represent a verification deadline for a particular course.

    The verification deadline is the datetime after which
    users are no longer allowed to submit photos for initial verification
    in a course.

    Note that this is NOT the same as the "upgrade" deadline, after
    which a user is no longer allowed to upgrade to a verified enrollment.

    If no verification deadline record exists for a course,
    then that course does not have a deadline.  This means that users
    can submit photos at any time.

    .. no_pii:
    """
    class Meta(object):
        app_label = "verify_student"

    course_key = CourseKeyField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text=ugettext_lazy(u"The course for which this deadline applies"),
    )

    deadline = models.DateTimeField(
        help_text=ugettext_lazy(
            u"The datetime after which users are no longer allowed "
            "to submit photos for verification."
        )
    )

    # The system prefers to set this automatically based on default settings. But
    # if the field is set manually we want a way to indicate that so we don't
    # overwrite the manual setting of the field.
    deadline_is_explicit = models.BooleanField(default=False)

    ALL_DEADLINES_CACHE_KEY = "verify_student.all_verification_deadlines"

    @classmethod
    def set_deadline(cls, course_key, deadline, is_explicit=False):
        """
        Configure the verification deadline for a course.

        If `deadline` is `None`, then the course will have no verification
        deadline.  In this case, users will be able to verify for the course
        at any time.

        Arguments:
            course_key (CourseKey): Identifier for the course.
            deadline (datetime or None): The verification deadline.

        """
        if deadline is None:
            VerificationDeadline.objects.filter(course_key=course_key).delete()
        else:
            record, created = VerificationDeadline.objects.get_or_create(
                course_key=course_key,
                defaults={"deadline": deadline, "deadline_is_explicit": is_explicit}
            )

            if not created:
                record.deadline = deadline
                record.deadline_is_explicit = is_explicit
                record.save()

    @classmethod
    def deadlines_for_courses(cls, course_keys):
        """
        Retrieve verification deadlines for particular courses.

        Arguments:
            course_keys (list): List of `CourseKey`s.

        Returns:
            dict: Map of course keys to datetimes (verification deadlines)

        """
        all_deadlines = cache.get(cls.ALL_DEADLINES_CACHE_KEY)
        if all_deadlines is None:
            all_deadlines = {
                deadline.course_key: deadline.deadline
                for deadline in VerificationDeadline.objects.all()
            }
            cache.set(cls.ALL_DEADLINES_CACHE_KEY, all_deadlines)

        return {
            course_key: all_deadlines[course_key]
            for course_key in course_keys
            if course_key in all_deadlines
        }

    @classmethod
    def deadline_for_course(cls, course_key):
        """
        Retrieve the verification deadline for a particular course.

        Arguments:
            course_key (CourseKey): The identifier for the course.

        Returns:
            datetime or None

        """
        try:
            deadline = cls.objects.get(course_key=course_key)
            return deadline.deadline
        except cls.DoesNotExist:
            return None


@receiver(models.signals.post_save, sender=VerificationDeadline)
@receiver(models.signals.post_delete, sender=VerificationDeadline)
def invalidate_deadline_caches(sender, **kwargs):  # pylint: disable=unused-argument
    """Invalidate the cached verification deadline information. """
    cache.delete(VerificationDeadline.ALL_DEADLINES_CACHE_KEY)