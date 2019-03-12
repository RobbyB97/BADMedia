"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
import json
import logging

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Image(Media):


    def __init__(self, dir, filename = None):
        # Set base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
        self.name = self.jsonobject['name']
        self.media = self.jsonobject['media']
