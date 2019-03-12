"""

    Author: Robby Bergers

    This is the class used to handle text type media

"""

# External Libraries
import os
import json
import logging

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Text(Media):


    def __init__(self, dir, filename = None):
        log.info('New Text class initializing...')

        Media.__init__(self, dir, filename = None)
        return


    def getInfo(self):
        log.info('Text.getInfo started...')

        # Set media type and pass to Media class
        self.type = 'text'
        Media.getInfo(self)
        return


    def getHTML(self):
        log.info('Text.getHTML started...')

        # Parse HTML post template
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/text/post.html', 'r') as f:
                self.wrap = f.read.split('|')
        except Exception:
            log.exception('Could not find text post template...')
