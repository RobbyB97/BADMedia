"""

    Author: Robby Bergers

    This file contains the functions used to generate the HTML output

"""

# External Libraries
import os
import json
import logging
import eyed3
import requests
from time import sleep

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

# Set Logger
log = logging.getLogger('BADMedia')
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



""" Make blog sections """
# (source = json object)
def makeAudio(source):

    log.info('makeAudio started:')
    os.chdir(jsondir)

    audio = [] # HTML output

    # Get audio template
    try:
        os.chdir(webdir)
        with open('./assets/templates/audio/post.html', 'r') as f:
            audiowrap = f.read().split('|')
    except Exception:
        log.exception('Could not find audio post template..')

    i=0 # Counter
    try:
        for media in source['media']:
            if i < 10:
                link = source['media'][media]
                audio.append(audiowrap[1])
                audio.append(source['name'])
                audio.append(audiowrap[2])
                audio.append(link)
                audio.append(audiowrap[3])
                i += 1
            else:
                break
    except Exception:
        log.exception('Could not write audio section HTML...')

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
        os.chdir(jsondir)
        if object.split('.')[1] != 'txt':
            try:
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

            except Exception:
                log.exception('%s cannot be opened...')
                continue

    # Get static templates
    os.chdir(webdir)
    with open('assets/templates/header.html', 'r') as f:
        html = f.read().split('|')
        header = html[1]
        footer = html[2]
    with open('assets/templates/topbar.html', 'r') as f:
        topbar = f.read()
    with open('assets/templates/pages.html', 'r') as f:
        pages = f.read().split('|') # Look at pages.html for list info

    # Write to index.html
    with open('index.html', 'w') as f:
        f.write(header)
        f.write(topbar)
        f.write(pages[1])
        i = 0
        while i < len(audio):
            j = 0
            while j < len(audio[i]):
                f.write(audio[i][j])
                j += 1
            i += 1
        f.write(pages[2])
        for seg in youtube:
            seg = str(seg)
            f.write(seg)
        f.write(pages[3])
        for seg in image:
            seg = str(seg)
            f.write(seg)
        f.write(pages[4])
        for seg in text:
            seg = str(seg)
            f.write(seg)
        f.write(pages[5])
        # TODO: Fill with content
        f.write(footer)

    return
