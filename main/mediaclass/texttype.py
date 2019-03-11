"""

    Author: Robby Bergers

    This is the class used to handle text type media

"""

import os
import app
import jsonhandler
import json
import logging

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

# Set Logger
log = logging.getLogger('BADMedia')



class Text:
    def __init__(self, filename):
        self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
        self.name = self.jsonobject['name']
        self.media = self.jsonobject['media']
