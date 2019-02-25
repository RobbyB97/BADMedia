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

appdir = os.path.dirname(os.path.realpath(__file__))
#logger
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)
handlerpath = appdir + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)
log.info('Running file ~/main/app.py:')

""" Clear json object in json file """
def clearJSON(object):
    os.chdir('%s/json/' % appdir)
    try:
        os.remove('%s.json' % object)
    except:
        log.warning('%s.json doesn\'t exist' % object)

""" Reconstruct JSON object with refreshed media links """
def getMedia():
    log.info('getMedia started:')
    try:
        os.chdir('%s/json/' % appdir)
        #TODO: Download media files
    except Exception:
        log.exception('Error in getMedia:')

""" Construct JSON object for HTML page"""
def getInfo():
    log.info('getInfo started:')
    try:

        # Set variables
        masterdict = {} # Final JSON object
        mediadict = {} # List of links to media

        # Get info on media from user
        mediatype = str(input('What type of media is this? [audio, video, image, text, youtube]\n'))
        masterdict['type'] = mediatype
        medianame = str(input('What will you call this media?\n'))
        masterdict['name'] = medianame
        link = str(input('Enter the link to the RSS feed:\n'))
        masterdict['xml'] = link
        tagname = str(input('Enter tagname containing media: [Default: enclosure]\n'))
        if not tagname:
            tagname = 'enclosure'
        masterdict['tag'] = tagname

        # Get XML file, scrape for media links
        xml = requests.get(link).text
        soup = bs(xml, "lxml")
        i=0
        for element in soup.findAll(tagname):
            mediadict[str(i)] = element['url']
            i += 1
        log.info('Found %s files in XML' % str(len(mediadict)))
        masterdict['media'] = mediadict

        # Create JSON object and write to file
        jsonfile = open('./json/%s.json' % medianame, 'w+')
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        jsonfile.write(json_str)
        jsonfile.close()
        log.info('%s json list created...' % medianame)
        jsonfile.close()

        # Add media to list
        try:
            medialist = open('jsonlist.txt', 'r')
            names = medialist.read().split(',')
            medialist.close()
            if medianame not in names:
                log.info('Adding %s to jsonlist...' % medianame)
                medialist = open('jsonlist.txt', 'a')
                medialist.write(',%s' % medianame)
                medialist.close()
        except:
            log.warning('jsonlist.txt not found, creating file...')
            medialist = open('jsonlist.txt', 'w')
            medialist.write('%s,' % medianame)
            medialist.close()

    except Exception:
        log.exception('Error in getInfo:')

if __name__ == '__main__':
    log.info('app.py started:')
    os.chdir(appdir)
    try:
        getInfo()
    except Exception:
        log.exception('Error in main process')
