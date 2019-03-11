"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
import app
import json
import logging

# Set Logger
log = logging.getLogger('BADMedia')


class Audio:

    def __init__(self, dir, filename = None):
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir
        if filename:    # If reference to json file exists
            self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
            self.name = self.jsonobject['name']
            self.media = self.jsonobject['media']
        else:       # If this is a new media object
            self.createJSON()

    # Get information from user to create JSON object and file
    def createJSON(self):
        self.name = str(input('What should this media be called?'))
