
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
from bs4 import BeautifulSoup

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


""" Scrape media """
def getText():
    try:

    except Exception:
        log.Exception('Error in getText:')
def getYoutube():
    try:

    except Exception:
        log.Exception('Error in getYoutube:')
def getImage():
    try:

    except Exception:
        log.Exception('Error in getImage:')
def getVideo():
    try:

    except Exception:
        log.Exception('Error in getVideo:')
def getAudio():
    try:

    except Exception:
        log.Exception('Error in getYoutube:')


""" Select mediatype to scrape """
def getInfo():
    log.info('getInfo started...')
    try:
        inp = input(print('What type of media would you like to gather? [text, audio, video, image or youtube]'))
        if (inp == 'text'):
            log.info('Text mediatype selected...')
            getText()
        elif (inp == 'audio'):
            log.info('Audio mediatype selected...')
            getAudio()
        elif (inp == 'video'):
            log.info('Video mediatype selected...')
            getVideo()
        elif (inp == 'image'):
            log.info('Image mediatype selected...')
            getImage()
        elif (inp == 'youtube'):
            log.info('Youtube mediatype selected...')
            getYoutube()
        else:
            log.info('%s is not a valid media type...')
            getInfo()
    except Exception:
        log.Exception('getInfo error:')
        getInfo()


if __name__ == '__main__':
    try:
        getInfo()
    except Exception:
        log.exception('Error in main process')
