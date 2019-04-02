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

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



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

            # Initialize podcast class
            self.podcast = Podcast(self.link)
            self.getMedia()

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
        log.debug('%s.getMedia started...' % self.name)

        self.media = {}

        # Get iframes
        self.media['iframes'] = self.podcast.iframes()

        # Get older episodes
        self.media['mp3'] = []
        for element in self.podcast.mp3list:
            try:
                x = self.media['iframes'][element['title']]
                log.debug('%s is an iframe, removing from list of mp3 files...' % element['title'])
            except:
                log.debug('adding %s to list of mp3 files' % element['title'])
                self.media['mp3'].append(element)
        return


    def updateJSON(self):
        log.debug('%s.updateJSON started...' % self.name)

        self.getMedia()     # Refresh post entries

        # Construct dictionary
        masterdict = {} # Final JSON object
        masterdict['type'] = self.type
        masterdict['name'] = self.name
        masterdict['xml'] = self.link
        masterdict['media'] = self.media

        # Store in JSON file
        os.chdir(self.dir['json'])
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        with open('%s.json' % self.name, 'w+') as f:
            f.write(json_str)
        return
