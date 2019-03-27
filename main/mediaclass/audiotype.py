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

        self.link = str(input('Enter the link to the feed:'))

        # Use libpyn if this is a libsyn link
        if 'libsyn' in self.link:
            log.info('libsyn podcast detected...')

            # Create podcast class and load class attributes
            self.podcast = Podcast(self.link)
            self.name = self.podcast.name

        else:
            Media.getInfo(self)
        return


    def getMedia(self):
        log.debug('Audio.getMedia started...')

        # Use the libsyn package if it's a libsyn podcast
        if 'libsyn' in self.link:
            log.info('Libsyn XML detected...')

        else:
            pass

    def getMediaLibsyn(self):
        log.debug('%s.getMediaLibsyn started...' % self.name)

        self.media = {}     # Reset list of audio links

        # Get XML file
        try:
            xml = requests.get(self.link).text
            soup = bs(xml, "lxml")
            log.info('Parsing %s...' % self.link)
        except Exception:
            log.exception('Error loading XML from %s...' % self.link)
            return

        # Loop through each item, get contents
        for element in soup.findAll('item'):
            try:
                title = element.find('title').text
                link = element.find(self.tag)['url']
                self.media[title] = link
            except:
                log.warning('Item not formatted properly. Skipping...')
                continue

        log.info('%s files found in %s...' % (len(self.media), self.link))
        return
