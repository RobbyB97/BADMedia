"""

    Author: Robby Bergers

    This is the class used to handle youtube type media

"""

# External Libraries
import os
import json
import logging

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Youtube(Media):


    def __init__(self, dir, filename = None):
        log.info('New Youtube class initializing...')

        Media.__init__(self, dir, filename = None)
        return


    def getInfo(self):
        log.info('Youtube.getInfo started...')

        # Set media type and pass to Media class
        self.type = 'youtube'
        Media.getInfo(self)
        return
