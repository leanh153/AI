

(function(globals) {

  var django = globals.django || (globals.django = {});

  
  django.pluralidx = function(n) {
    var v=0;
    if (typeof(v) == 'boolean') {
      return v ? 1 : 0;
    } else {
      return v;
    }
  };
  

  /* gettext library */

  django.catalog = django.catalog || {};
  
  var newcatalog = {
    "%(sel)s of %(cnt)s selected": [
      "%(sel)s \u0e08\u0e32\u0e01 %(cnt)s selected"
    ], 
    "6 a.m.": "\u0e2b\u0e01\u0e42\u0e21\u0e07\u0e40\u0e0a\u0e49\u0e32", 
    "Available %s": "%s\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48", 
    "Cancel": "\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", 
    "Changes to steps that are not selected as part of the assignment will not be saved.": "\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e43\u0e19\u0e02\u0e31\u0e49\u0e19\u0e15\u0e2d\u0e19\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e43\u0e2b\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e02\u0e2d\u0e07\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e21\u0e2d\u0e1a\u0e2b\u0e21\u0e32\u0e22\u0e08\u0e30\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", 
    "Choose": "\u0e40\u0e25\u0e37\u0e2d\u0e01", 
    "Choose a time": "\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e27\u0e25\u0e32", 
    "Choose all": "\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", 
    "Chosen %s": "%s\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e40\u0e25\u0e37\u0e2d\u0e01", 
    "Click to choose all %s at once.": "\u0e04\u0e25\u0e34\u0e01\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e25\u0e37\u0e2d\u0e01 %s \u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27", 
    "Click to remove all chosen %s at once.": "\u0e04\u0e25\u0e34\u0e01\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e2d\u0e32 %s \u0e2d\u0e2d\u0e01\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27", 
    "Could not retrieve download url.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e40\u0e23\u0e35\u0e22\u0e01 url \u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14", 
    "Could not retrieve upload url.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e40\u0e23\u0e35\u0e22\u0e01 url \u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e2d\u0e31\u0e1e\u0e42\u0e2b\u0e25\u0e14", 
    "Couldn't Save This Assignment": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e1c\u0e25\u0e07\u0e32\u0e19\u0e19\u0e35\u0e49", 
    "Criterion Added": "\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e1e\u0e34\u0e08\u0e32\u0e23\u0e13\u0e32\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21", 
    "Criterion Deleted": "\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e1e\u0e34\u0e08\u0e32\u0e23\u0e13\u0e32\u0e16\u0e39\u0e01\u0e25\u0e1a", 
    "Error": "\u0e1c\u0e34\u0e14\u0e1e\u0e25\u0e32\u0e14", 
    "Filter": "\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07", 
    "Hide": "\u0e0b\u0e48\u0e2d\u0e19", 
    "Midnight": "\u0e40\u0e17\u0e35\u0e48\u0e22\u0e07\u0e04\u0e37\u0e19", 
    "Noon": "\u0e40\u0e17\u0e35\u0e48\u0e22\u0e07\u0e27\u0e31\u0e19", 
    "Not Selected": "\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e40\u0e25\u0e37\u0e2d\u0e01", 
    "Now": "\u0e02\u0e13\u0e30\u0e19\u0e35\u0e49", 
    "One or more rescheduling tasks failed.": "\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e25\u0e49\u0e21\u0e40\u0e2b\u0e25\u0e27\u0e43\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07", 
    "Option Deleted": "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e16\u0e39\u0e01\u0e25\u0e1a", 
    "Please correct the outlined fields.": "\u0e01\u0e23\u0e38\u0e13\u0e32\u0e41\u0e01\u0e49\u0e44\u0e02\u0e0a\u0e48\u0e2d\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e44\u0e27\u0e49", 
    "Remove": "\u0e25\u0e1a\u0e2d\u0e2d\u0e01", 
    "Remove all": "\u0e40\u0e2d\u0e32\u0e2d\u0e2d\u0e01\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", 
    "Saving...": "\u0e01\u0e33\u0e25\u0e31\u0e07\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01...", 
    "Show": "\u0e41\u0e2a\u0e14\u0e07", 
    "Status of Your Response": "\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13", 
    "The server could not be contacted.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e40\u0e0b\u0e34\u0e1f\u0e40\u0e27\u0e2d\u0e23\u0e4c", 
    "The submission could not be removed from the grading pool.": "\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e25\u0e1a\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e1c\u0e25\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19", 
    "This assessment could not be submitted.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e2a\u0e48\u0e07\u0e01\u0e32\u0e23\u0e30\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49", 
    "This feedback could not be submitted.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e2a\u0e48\u0e07\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49", 
    "This is the list of available %s. You may choose some by selecting them in the box below and then clicking the \"Choose\" arrow between the two boxes.": "\u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49\u0e02\u0e2d\u0e07 %s \u0e04\u0e38\u0e13\u0e2d\u0e32\u0e08\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1a\u0e32\u0e07\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e42\u0e14\u0e22\u0e01\u0e32\u0e23\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e41\u0e25\u0e49\u0e27\u0e04\u0e25\u0e34\u0e01\u0e17\u0e35\u0e48\u0e1b\u0e38\u0e48\u0e21 \"\u0e40\u0e25\u0e37\u0e2d\u0e01\" \u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e2a\u0e2d\u0e07\u0e01\u0e25\u0e48\u0e2d\u0e07", 
    "This is the list of chosen %s. You may remove some by selecting them in the box below and then clicking the \"Remove\" arrow between the two boxes.": "\u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e02\u0e2d\u0e07 %s \u0e04\u0e38\u0e13\u0e2d\u0e32\u0e08\u0e40\u0e2d\u0e32\u0e1a\u0e32\u0e07\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e42\u0e14\u0e22\u0e01\u0e32\u0e23\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e41\u0e25\u0e49\u0e27\u0e04\u0e25\u0e34\u0e01\u0e17\u0e35\u0e48\u0e1b\u0e38\u0e48\u0e21 \"\u0e40\u0e2d\u0e32\u0e2d\u0e2d\u0e01\" \u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e2a\u0e2d\u0e07\u0e01\u0e25\u0e48\u0e2d\u0e07", 
    "This problem could not be saved.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49", 
    "This problem has already been released. Any changes will apply only to future assessments.": "\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1b\u0e25\u0e48\u0e2d\u0e22\u0e01\u0e48\u0e2d\u0e19\u0e41\u0e25\u0e49\u0e27 \u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e43\u0e14\u0e46\u0e08\u0e30\u0e43\u0e0a\u0e49\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e1c\u0e25\u0e43\u0e19\u0e2d\u0e19\u0e32\u0e04\u0e15", 
    "This response could not be saved.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49", 
    "This response could not be submitted.": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49", 
    "This response has been saved but not submitted.": "\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2a\u0e48\u0e07\u0e43\u0e2b\u0e49\u0e1e\u0e34\u0e08\u0e32\u0e23\u0e13\u0e32\u0e15\u0e48\u0e2d\u0e44\u0e1b", 
    "This response has not been saved.": "\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", 
    "This section could not be loaded.": "\u0e40\u0e19\u0e37\u0e49\u0e2d\u0e2b\u0e32\u0e2a\u0e48\u0e27\u0e19\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e42\u0e2b\u0e25\u0e14\u0e44\u0e14\u0e49", 
    "Today": "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49", 
    "Tomorrow": "\u0e1e\u0e23\u0e38\u0e48\u0e07\u0e19\u0e35\u0e49", 
    "Type into this box to filter down the list of available %s.": "\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e25\u0e07\u0e43\u0e19\u0e0a\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e01\u0e23\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49\u0e02\u0e2d\u0e07 %s", 
    "Unnamed Option": "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e0a\u0e37\u0e48\u0e2d", 
    "Warning": "\u0e04\u0e33\u0e40\u0e15\u0e37\u0e2d\u0e19", 
    "Yesterday": "\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e27\u0e32\u0e19", 
    "You have selected an action, and you haven't made any changes on individual fields. You're probably looking for the Go button rather than the Save button.": "\u0e04\u0e38\u0e13\u0e44\u0e14\u0e49\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e41\u0e25\u0e30\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e17\u0e33\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e43\u0e14 \u0e46 \u0e43\u0e19\u0e1f\u0e34\u0e25\u0e14\u0e4c \u0e04\u0e38\u0e13\u0e2d\u0e32\u0e08\u0e21\u0e2d\u0e07\u0e2b\u0e32\u0e1b\u0e38\u0e48\u0e21\u0e44\u0e1b\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e1b\u0e38\u0e48\u0e21\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", 
    "You have selected an action, but you haven't saved your changes to individual fields yet. Please click OK to save. You'll need to re-run the action.": "\u0e04\u0e38\u0e13\u0e44\u0e14\u0e49\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07 \u0e41\u0e15\u0e48\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e44\u0e1b\u0e22\u0e31\u0e07\u0e1f\u0e34\u0e25\u0e14\u0e4c \u0e01\u0e23\u0e38\u0e13\u0e32\u0e04\u0e25\u0e34\u0e01 OK \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01 \u0e04\u0e38\u0e13\u0e08\u0e30\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07", 
    "You have unsaved changes on individual editable fields. If you run an action, your unsaved changes will be lost.": "\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e43\u0e19\u0e41\u0e15\u0e48\u0e25\u0e30\u0e1f\u0e34\u0e25\u0e14\u0e4c \u0e16\u0e49\u0e32\u0e04\u0e38\u0e13\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e08\u0e30\u0e2b\u0e32\u0e22\u0e44\u0e1b", 
    "You're about to submit your response for this assignment. After you submit this response, you can't change it or submit a new response.": "\u0e04\u0e38\u0e13\u0e44\u0e14\u0e49\u0e2a\u0e48\u0e07\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e19\u0e35\u0e49 \u0e2b\u0e25\u0e31\u0e07\u0e08\u0e32\u0e01\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e49\u0e27 \u0e04\u0e38\u0e13\u0e08\u0e30\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e2a\u0e48\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2d\u0e35\u0e01"
  };
  for (var key in newcatalog) {
    django.catalog[key] = newcatalog[key];
  }
  

  if (!django.jsi18n_initialized) {
    django.gettext = function(msgid) {
      var value = django.catalog[msgid];
      if (typeof(value) == 'undefined') {
        return msgid;
      } else {
        return (typeof(value) == 'string') ? value : value[0];
      }
    };

    django.ngettext = function(singular, plural, count) {
      var value = django.catalog[singular];
      if (typeof(value) == 'undefined') {
        return (count == 1) ? singular : plural;
      } else {
        return value[django.pluralidx(count)];
      }
    };

    django.gettext_noop = function(msgid) { return msgid; };

    django.pgettext = function(context, msgid) {
      var value = django.gettext(context + '\x04' + msgid);
      if (value.indexOf('\x04') != -1) {
        value = msgid;
      }
      return value;
    };

    django.npgettext = function(context, singular, plural, count) {
      var value = django.ngettext(context + '\x04' + singular, context + '\x04' + plural, count);
      if (value.indexOf('\x04') != -1) {
        value = django.ngettext(singular, plural, count);
      }
      return value;
    };

    django.interpolate = function(fmt, obj, named) {
      if (named) {
        return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
      } else {
        return fmt.replace(/%s/g, function(match){return String(obj.shift())});
      }
    };


    /* formatting library */

    django.formats = {
    "DATETIME_FORMAT": "j F Y, G:i", 
    "DATETIME_INPUT_FORMATS": [
      "%d/%m/%Y %H:%M:%S.%f", 
      "%d/%m/%Y %H:%M:%S", 
      "%d/%m/%Y %H:%M", 
      "%Y-%m-%d %H:%M:%S", 
      "%Y-%m-%d %H:%M:%S.%f", 
      "%Y-%m-%d %H:%M", 
      "%Y-%m-%d"
    ], 
    "DATE_FORMAT": "j F Y", 
    "DATE_INPUT_FORMATS": [
      "%d/%m/%Y", 
      "%d %b %Y", 
      "%d %B %Y", 
      "%Y-%m-%d"
    ], 
    "DECIMAL_SEPARATOR": ".", 
    "FIRST_DAY_OF_WEEK": "0", 
    "MONTH_DAY_FORMAT": "j F", 
    "NUMBER_GROUPING": "3", 
    "SHORT_DATETIME_FORMAT": "j M Y, G:i", 
    "SHORT_DATE_FORMAT": "j M Y", 
    "THOUSAND_SEPARATOR": ",", 
    "TIME_FORMAT": "G:i", 
    "TIME_INPUT_FORMATS": [
      "%H:%M:%S.%f", 
      "%H:%M:%S", 
      "%H:%M"
    ], 
    "YEAR_MONTH_FORMAT": "F Y"
  };

    django.get_format = function(format_type) {
      var value = django.formats[format_type];
      if (typeof(value) == 'undefined') {
        return format_type;
      } else {
        return value;
      }
    };

    /* add to global namespace */
    globals.pluralidx = django.pluralidx;
    globals.gettext = django.gettext;
    globals.ngettext = django.ngettext;
    globals.gettext_noop = django.gettext_noop;
    globals.pgettext = django.pgettext;
    globals.npgettext = django.npgettext;
    globals.interpolate = django.interpolate;
    globals.get_format = django.get_format;

    django.jsi18n_initialized = true;
  }

}(this));
