"""
Serializers to be used in APIs.
"""

from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey, UsageKey
from rest_framework import serializers


class CollapsedReferenceSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes arbitrary models in a collapsed format, with just an id and url."""
    url = serializers.HyperlinkedIdentityField(view_name='')

    def __init__(self, model_class, view_name, id_source='id', lookup_field=None, *args, **kwargs):
        """Configures the serializer.

        Args:
            model_class (class): Model class to serialize.
            view_name (string): Name of the Django view used to lookup the
                model.
            id_source (string): Optional name of the id field on the model.
                Defaults to 'id'. Also used as the property name of the field
                in the serialized representation.
            lookup_field (string): Optional name of the model field used to
                lookup the model in the view. Defaults to the value of
                id_source.
        """
        if not lookup_field:
            lookup_field = id_source

        self.Meta.model = model_class

        super(CollapsedReferenceSerializer, self).__init__(*args, **kwargs)

        self.fields[id_source] = serializers.CharField(read_only=True)
        self.fields['url'].view_name = view_name
        self.fields['url'].lookup_field = lookup_field
        self.fields['url'].lookup_url_kwarg = lookup_field

    class Meta(object):
        fields = ("url",)


class CourseKeyField(serializers.Field):
    """ Serializer field for a model CourseKey field. """

    def to_representation(self, data):
        """Convert a course key to unicode. """
        return unicode(data)

    def to_internal_value(self, data):
        """Convert unicode to a course key. """
        try:
            return CourseKey.from_string(data)
        except InvalidKeyError as ex:
            raise serializers.ValidationError(u"Invalid course key: {msg}".format(msg=ex.msg))


class UsageKeyField(serializers.Field):
    """ Serializer field for a model UsageKey field. """

    def to_representation(self, data):
        """Convert a usage key to unicode. """
        return unicode(data)

    def to_internal_value(self, data):
        """Convert unicode to a usage key. """
        try:
            return UsageKey.from_string(data)
        except InvalidKeyError as ex:
            raise serializers.ValidationError(u"Invalid usage key: {msg}".format(msg=ex.msg))