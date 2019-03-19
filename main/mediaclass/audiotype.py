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


    def getMedia(self):
        log.debug('Audio.getMedia started...')

        if 'libsyn' in self.link:
            log.info('Libsyn XML detected...')
            self.getMediaLibsyn(self)
        else:
            pass

    def getMediaLibsyn(self):
        log.debug('%s.getMediaLibsyn started...' % self.name)

        self.media = {}     # Reset list of audio links

        # Get XML file
        try:
            xml = requests.get(self.link).text
            soup = bs(xml, "lxml")
        except Exception:
            log.exception('Error loading XML from %s...' % self.link)
            return

        # Loop through each item, get contents
        for element in soup.findAll('item'):
            title = element.find('title').text
            link = element.find(self.tag)['url']
            self.media[title] = link

        for element in self.media:
            print('Title: \n %s \n\n Link: \n %s \n\n' % (element, self.media[element]))
        return
