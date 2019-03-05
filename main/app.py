"""

    Author: Robby Bergers

    This is the main file for gathering media, constructing JSON objects
    from it and downloading media locally

"""

import requests
from urllib import request
import os
from time import sleep
import logging
import json
import pytube
from bs4 import BeautifulSoup as bs

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

# Set Logger
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



""" Ensure jsonlist matches JSON objects """
def cleanJSONList():

    log.info('cleanJSONList started:')
    os.chdir(appdir)

    jsonobjects = []
    jsons = os.listdir('%s/json/' % appdir)
    for object in jsons:
        if object.split('.')[1] == 'json':
            jsonobjects.append(object.split('.')[0])

    with open('jsonlist.txt', 'w') as file:
        for name in jsonobjects:
            file.write('%s,' % name)

    return



""" Load json object """
def loadJSON(object):

    log.info('loadJSON started:')
    os.chdir(appdir)

    try:
        print('lol')
        return
    except Exception:
        log.exception('Error loading json file')
        return



""" Clear all JSON objects """
def clearAllJSON():

    log.info('clearAllJSON started:')
    os.chdir('%s/json/' % appdir)

    filelist = os.listdir()
    for file in filelist:
        name = file.split('.')[0]
        clearJSON(name)

    return



""" Clear specific json object """
def clearJSON(object):

    log.info('clearJSON(%s) started:' % object)
    os.chdir(jsondir)

    # Remove json file
    try:
        os.remove('%s.json' % object)
    except:
        log.warning('%s.json doesn\'t exist' % object)
        return

    # Get jsonlist names
    os.chdir(appdir)
    medialist = open('jsonlist.txt', 'r')
    names = medialist.read().strip('\n').split(',')
    print(names)
    medialist.close()

    # Clear object from jsonlist
    medialist = open('jsonlist.txt', 'w')
    for name in names:
        if name is object:
            names.remove(name)
        else:
            if name is not '':
                medialist.write('%s,' % name)
    medialist.close()

    return



""" Reconstruct JSON object with refreshed media links """
def getMedia(object):

    log.info('getMedia started:')
    os.chdir(jsondir)

    # TODO: Download media locally

    return



""" Construct JSON object for HTML page"""
def getInfo():

    log.info('getInfo started:')
    os.chdir(appdir)

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

        return

    except:
        log.warning('jsonlist.txt not found, creating file...')
        medialist = open('jsonlist.txt', 'w')
        medialist.write('%s,' % medianame)
        medialist.close()

        return



""" Make blog sections """
# (source = json object)
def makeAudio(source):

    log.info('makeAudio started:')
    os.chdir(jsondir)

    #TODO: add posts to proper html template


    return audio

def makeYoutube(source):

    log.info('makeYoutube started:')
    os.chdir(jsondir)

    #TODO: add posts to proper html template

    return youtube

def makeImage(source):

    log.info('makeImage started:')
    os.chdir(jsondir)

    #TODO: add posts to proper html template

    return image

def makeText(source):

    log.info('makeText started:')
    os.chdir(jsondir)

    #TODO: add posts to proper html template

    return text



""" Generate HTML File """
def createPage():

    log.info('createPage started:')
    os.chdir(webdir)

    # Media HTML lists
    audio = []
    youtube = []
    text = []
    image = []

    # Iterate through json files to turn media into HTML
    os.chdir(jsondir)
    for object in os.listdir(jsondir):
        if object.split('.')[1] != 'txt':
            with open(object, 'r') as f:
                source = json.loads(f.read())

                # Make proper media HTML generator function call based on type
                if source['type'] == 'audio':
                    post = makeAudio(source)
                    audio.append(post)
                elif source['type'] == 'youtube':
                    post = makeYoutube(source)
                    youtube.append(post)
                elif source['type'] == 'image':
                    post = makeImage(source)
                    image.append(post)
                elif source['type'] == 'text':
                    post = makeText(source)
                    text.append(post)
                else:
                    log.warning('%s is not a usable media type' % source['type'])

    # Get static templates
    os.chdir(webdir)
    with open('assets/templates/header.html', 'r') as f:
        html = f.read().split('|')
        header = html[1]
        footer = html[2]
    with open('assets/templates/topbar.html', 'r') as f:
        topbar = f.read()
    with open('assets/templates/pages.html', 'r') as f:
        # Look at pages.html for list info
        pages = f.read().split('|')
        pages.pop(0)

    # Write to index.html
    with open('index.html', 'w') as f:
        f.write(header)
        f.write(topbar)
        for page in pages:
            f.write(page)
        # TODO: Fill with content
        f.write(footer)

    return



def mainMenu():

    log.info('mainMenu started:')
    os.chdir(appdir)

    inp = str(input('What would you like to do?\n\
    add: add new media source\n\
    clear: remove a media source\n\
    clearall: clear all media sources\n\
    create: generate webpage\n\
    exit: exit.\n'))
    if inp == 'add':
        getInfo()
    elif inp == 'clear':
        source = str(input('Which source do you want to remove?'))
        clearJSON(source)
    elif inp == 'clearall':
        clearAllJSON()
    elif inp == 'create':
        createPage()
    elif inp == 'exit':
        break
    else:
        print('Input invalid!')

    return


""" Main Process """
if __name__ == '__main__':

    log.info('app.py started:')
    os.chdir(appdir)

    try:
        makeAudio()
        return

    except Exception:
        log.exception('Error in main process')
        return
