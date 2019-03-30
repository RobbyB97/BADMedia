"""

    Author: Robby Bergers

    This is the class used to handle libsyn podcasts

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests
import time
from libpyn.podcast import Podcast

class Libsyn(Media):


    def __init__(self, dir, filename=None):

        # Set attributes
        self.type = 'libsyn'
        self.dir = dir

        # Load JSON object (if filename argument passed)
        if filename:
            try:
                os.chdir(self.dir['json'])
                with open(filename, 'r') as f:
                    jsonobject = json.loads(f.read())
            except:
                log.warning('Error loading %s.json. Creating new media source...' % filename)
                self.getInfo()

            # Assign class attributes from JSON object
            self.name = jsonobject['name']
            self.link = jsonobject['xml']
            self.media = jsonobject['media']

        else:
            self.getInfo()
        return


    def getInfo(self):
        log.debug('Libsyn.getInfo started...')

        # Get link from user, initialize as Podcast class
        self.link = str(input('Enter the link to the podcast:'))

        self.podcast = Podcast(self.link)
        self.name = self.podcast.name

        self.updateJSON()
        return


    def getMedia(self):
        return


    def updateJSON(self):
        return


    def clearJSON(self):
        return
