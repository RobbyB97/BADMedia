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
import time
from libpyn.podcast import Podcast

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Audio(Media):


    def __init__(self, dir, filename = None):

        self.type = 'audio'

        if filename:
            Media.__init__(self, dir=dir, filename=filename)
        else:
            Media.__init__(self, dir=dir)

        log.info('%s loaded...' % self.name)
        return


    def getInfo(self):
        pass


    def getMedia(self):
        pass
