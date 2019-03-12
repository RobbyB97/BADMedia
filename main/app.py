"""

    Author: Robby Bergers

    This is the main file containing the BADMedia class

"""

# External Libraries
import sys
import requests
import os
from time import sleep
import logging
import json
from bs4 import BeautifulSoup as bs

# Internal Libraries
from mediaclass import audiotype
from htmlclass import htmlwriter as html
from mediaclass import youtubetype
from mediaclass import imagetype
from mediaclass import texttype

# Set Logger
log = logging.getLogger('BADMedia')
log.setLevel(logging.WARNING)
handlerpath = os.path.dirname(os.path.realpath(__file__)) + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)
log.info('Running file ~/main/app.py:')



class BADMedia:


    def __init__(self):
        log.info('New BADMedia class initializing...')

        # Base Directory
        self.appdir = os.path.dirname(os.path.realpath(__file__))
        self.jsondir = '%s/json/' % self.appdir
        self.webdir = '%s/../docs/' % self.appdir

        # Create class lists / html writer class instance
        self.htmls = html.Writer(dir=self.appdir)
        self.audios = []
        self.youtubes = []
        self.images = []
        self.texts = []


    def menu(self):
        log.info('menu started:')
        os.chdir(self.appdir)

        inp = str(input('What would you like to do?\n\
        add: add new media source\n\
        clear: remove a media source\n\
        clearall: clear all media sources\n\
        create: generate webpage\n\
        exit: exit.\n'))

        if inp == 'add':
            answer = str(input('What type of media?\n\
            audio: an podcast or other audio stream\n\
            youtube: a youtube channel\n\
            image: an image feed\n\
            text: a text article feed\n\
            back: back to menu.\n'))
            if answer == 'audio':
                media = audiotype.Audio(dir=self.appdir)
                self.audios.append(media)
            elif answer == 'youtube':
                media = youtubetype.YouTube(dir=self.appdir)
                self.youtubes.append(media)
            elif answer == 'image':
                media = imagetype.Image(dir=self.appdir)
                self.images.append(media)
            elif answer == 'text':
                media = texttype.Text(dir=self.appdir)
                self.texts.append(media)
            elif answer == 'back':
                self.menu()
            else:
                print('Input invalid!')
        #TODO: Add clear option
        #TODO: Add clearall option
        #TODO: Add create option
        else:
            print('Input invalid!')



if __name__ == '__main__':
    log.info('app.py started:')

    try:
        bad = BADMedia()
        bad.menu()

    except Exception:
        log.exception('Error in main process')
