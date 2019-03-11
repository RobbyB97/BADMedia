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
        # Set base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        if filename:    # If reference to json file exists
            self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']
            self.tag = self.jsonobject['tag']
        else:       # If this is a new media object
            self.getInfo()
        return

    def getInfo(self):
        # Get object information from user
        self.type = 'audio'
        self.name = str(input('What should this media be called?\n'))
        self.link = str(input('Enter the link to the feed:\n'))
        self.tag = str(input('Enter tag name containing media: [default = \'enclosure\']'))
        if not self.tag:
            self.tag = 'enclosure'

        self.saveToJSON()
        return
