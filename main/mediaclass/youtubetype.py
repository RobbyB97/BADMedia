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

        # Set media type and pass to Media class
        self.type = 'youtube'

        if filename:
            Media.__init__(self, dir=dir, filename=filename)
        else:
            Media.__init__(self, dir=dir)
        return


    def getHTML(self):
        log.info('Youtube.getHTML started...')

        # Parse HTML post template
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/youtube/post.html', 'r') as f:
                self.wrap = f.read.split('|')
        except Exception:
            log.exception('Could not find youtube post template...')
