"""

    Author: Robby Bergers

    This is the main file for gathering media, constructing JSON objects
    from it and downloading media locally

"""

# External Libraries
import requests
import os
from time import sleep
import logging
import json
import pytube
from bs4 import BeautifulSoup as bs

# Internal Libraries
import htmlgen
import jsonhandler as jso
import audiotype
import htmlwriter as html
import imagetype
import texttype
import youtubetype

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
log.info('Running file ~/main/app.py:')

# Variables for storing classes
audios = []         # Audio media object instances appended here
youtubes = []       # Youtube media object instances appended here
images = []         # Image media object instances appended here
texts = []          # Text media object instances appended here
htmler = html.Writer()  # Object that generates HTML file

""" Take user input to decide what to do """
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
        jso.getInfo()
    elif inp == 'clear':
        source = str(input('Which source do you want to remove?'))
        jso.clearJSON(source)
    elif inp == 'clearall':
        jso.clearAllJSON()
    elif inp == 'create':
        htmlgen.createPage()
    elif inp == 'exit':
        return
    else:
        print('Input invalid!')



""" Main Process """
if __name__ == '__main__':

    log.info('app.py started:')
    os.chdir(appdir)

    try:
        mainMenu()

    except Exception:
        log.exception('Error in main process')
