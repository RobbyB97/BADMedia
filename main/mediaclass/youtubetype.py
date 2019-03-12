"""

    Author: Robby Bergers

    This is the class used to handle youtube type media

"""

# External Libraries
import os
import json
import logging

# Internal Libraries
import media

# Set Logger
log = logging.getLogger('BADMedia')



class Youtube:
    def __init__(self, dir, filename = None):
        self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
        self.name = self.jsonobject['name']
        self.media = self.jsonobject['media']
