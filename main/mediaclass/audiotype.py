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
import eyed3
import time

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Audio(Media):


    def __init__(self, dir, filename = None):

        # Set Audio-specific attributes
        self.type = 'audio'

        if filename:
            Media.__init__(self, dir=dir, filename=filename)
        else:
            Media.__init__(self, dir=dir)
        return


    def getName2(self):
        log.debug('Audio.getName2 started...')

        # Get XML file
        xml = requests.get(self.link).text
        soup = bs(xml, 'lxml')

        # Parse titles
        for element in soup. findAll('title'):
            print(element.text)
        return
