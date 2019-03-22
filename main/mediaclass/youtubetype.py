"""

    Author: Robby Bergers

    This is the class used to handle youtube type media

"""

# External Libraries
import os
import json
import logging
from yt_iframe import yt

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Youtube(Media):


    def __init__(self, dir, filename = None):

        # Set media type and pass to Media class
        self.type = 'youtube'

        # Load JSON object (if filename argument passed)
        if filename:
            try:
                os.chdir(self.dir['json'])
                with open(filename, 'r') as f:
                    self.jsonobject = json.loads(f.read())
            except:
                log.warning('Error loading %s.json. Creating new media source...' % filename)
                self.getInfo()

            # Assign class attributes from JSON object
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']

        else:
            self.getInfo()
        return


    def getInfo(self):
        log.debug('Youtube.getInfo started...')

        # Get information from user
        self.name = str(input('What is the name of the Youtube channel?'))
        self.link = str(input('Enter the link to the channel:'))

        self.updateJSON()
        return
