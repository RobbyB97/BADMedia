
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


""" Construct JSON object """
def getInfo():
    log.debug('getInfo started:')
    try:
        # Set variables
        masterdict = {} # Final JSON object
        mediadict = {} # List of links to media
        mediatype = str(input('What type of media is this? [audio, video, image, text, youtube]'))
        medianame = str(input('What will you call this media?'))
        appdir = os.path.dirname(os.path.realpath(__file__))
        jsonfile = open('%s/json/%s.json' % (appdir, medianame), 'w+')
        link = str(input('Enter the link to the RSS feed:'))
        tagname = str(input('Enter tagname containing media: [Default: enclosure]'))
        if not tagname:
            tagname = 'enclosure'
        xml = requests.get(link).text
        soup = bs(xml, "lxml")
        i=0
        for element in soup.findAll(tagname):
            mediadict[str(i)] = element['url']
            i += 1
        log.info('Found %s files in XML' % str(len(mediadict)))
        # Create JSON object and write to file
        masterdict['media'] = mediadict
        masterdict['tagname'] = tagname
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        jsonfile.write(json_str)
        jsonfile.close()
        log.info('%s json list created...' % medianame)
        jsonfile.close()
        return
    except Exception:
        log.exception('Error in getInfo:')

if __name__ == '__main__':
    log.info('app.py started:')
    try:
        getInfo()
    except Exception:
        log.exception('Error in main process')
