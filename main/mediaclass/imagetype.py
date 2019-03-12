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
        log.info('New Image class initializing...')

        Media.__init__(self, dir, filename = None)
        return


    def getInfo(self):
        log.info('Image.getInfo started...')

        # Set media type and pass to Media class
        self.type = 'image'
        Media.getInfo(self)
        return


    def getHTML(self):
        log.info('Image.getHTML started...')

        # Parse HTML post template
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/image/post.html', 'r') as f:
                self.wrap = f.read.split('|')
        except Exception:
            log.exception('Could not find image post template...')
