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


    def getName(self):
        log.debug('Audio.getName started...')

        self.cachedir = '%s/cache/' % self.appdir

        for media in self.media:

            os.chdir(self.cachedir)
            time.sleep(1)       # Prevent IP ban

            # Download mp3 file to cache
            log.info('Saving mp3 file to cache...')
            with requests.get(self.media[media]) as mp3file:
                with open('mp3file.mp3', 'wb') as f:
                    for bit in mp3file.iter_content(chunk_size=8192):
                        log.info('Writing bit...')
                        f.write(bit)
            mp3 = eyed3.load('mp3file.mp3')
            title = mp3.tag.title
            if title:
                print(title)
                os.remove('mp3file.mp3')
            else:
                log.info('No titles given in mp3 meta for this feed...')
                os.remove('mp3file.mp3')
                return
