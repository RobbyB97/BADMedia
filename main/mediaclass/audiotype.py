"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Audio(Media):


    def __init__(self, dir, filename = None):
        log.info('New Audio class initializing...')

        Media.__init__(self, dir, filename = None)
        return


    def getInfo(self):
        log.info('Audio.getInfo started...')

        # Set media type and pass to Media class
        self.type = 'audio'
        Media.getInfo(self)
        return


    def getHTML(self):
        log.info('Audio.getHTML started...')

        # Parse HTML post template
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/audio/post.html', 'r') as f:
                self.wrap = f.read.split('|')
