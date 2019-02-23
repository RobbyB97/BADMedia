
"""
Author: Robby Bergers
Info: Gather media to be displayed on webpage
"""

import requests
from urllib import request
import os
from time import sleep
import logging
import json
import pytube
from bs4 import BeautifulSoup as bs

#logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.FileHandler('app.log')
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)
log.info('Running file ~/main/app.py:')


# Scrape Media, save data as json file
# and append medianame to list of json objects
def getText():
    log.debug('getText started:')
    try:

        return
    except Exception:
        log.exception('Error in getText:')
def getYoutube():
    log.debug('getYoutube started:')
    try:

        return
    except Exception:
        log.exception('Error in getYoutube:')
def getImage():
    log.debug('getImage started:')
    try:
        return
    except Exception:
        log.exception('Error in getImage:')
def getVideo():
    log.debug('getVideo started:')
    try:

        return
    except Exception:
        log.exception('Error in getVideo:')
def getAudio():
    log.debug('getAudio started:')
    try:
        # Set variables
        dict = {}
        medianame = str(input('What will you call this media?'))
        jsonfile = open('./json/%s.json' % medianame, 'w+')
        link = str(input('Enter the link to the RSS feed:'))
        xml = requests.get(link).text
        soup = bs(xml, "lxml")

        jsonfile.close()
        return
    except Exception:
        log.exception('Error in getYoutube:')

# Select mediatype to scrape
def getInfo():
    log.info('getInfo started...')
    try:
        inp = input(print('What type of media would you like to gather? [text, audio, video, image or youtube]'))
        if inp == 'text':
            log.info('Text mediatype selected...')
            getText()
        elif inp == 'audio':
            log.info('Audio mediatype selected...')
            getAudio()
        elif inp == 'video':
            log.info('Video mediatype selected...')
            getVideo()
        elif inp == 'image':
            log.info('Image mediatype selected...')
            getImage()
        elif inp == 'youtube':
            log.info('Youtube mediatype selected...')
            getYoutube()
        else:
            log.info('%s is not a valid media type...')
            getInfo()
    except Exception:
        log.exception('getInfo error:')
        getInfo()


if __name__ == '__main__':
    log.info('app.py started:')
    try:
        getInfo()
    except Exception:
        log.exception('Error in main process')
