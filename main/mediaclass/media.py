"""

    Author: Robby Bergers

    This is the master class for all media types

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests

# Internal Libraries
from mediaclass.audiotype import Audio
from mediaclass.imagetype import Image
from mediaclass.texttype import Text
from mediaclass.youtubetype import Youtube

# Set Logger
log = logging.getLogger('BADMedia')



class Media:


    def __init__(self, dir, filename = None):
        log.info('New Media class initializing...')

        # Set base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        if filename:    # If reference to json file exists
            try:
                self.jsonobject = json.loads('%s%s.json' % (self.jsondir, filename))
            except Exception:
                log.exception('Error loading %s.json. Creating new media source...')
                self.getInfo()
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']
            self.tag = self.jsonobject['tag']

        else:       # If this is a new media object
            self.getInfo()

        return


    def getInfo(self):
        print('MEDIA GETINFO')
