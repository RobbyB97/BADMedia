"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
import json
import logging

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

# Set Logger
log = logging.getLogger('BADMedia')



class Image:
    def __init__(self, filename):
        self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
        self.name = self.jsonobject['name']
        self.media = self.jsonobject['media']
