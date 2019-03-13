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
from mediaclass.audiotype import Audio
from htmlclass.htmlwriter import Writer
from mediaclass.youtubetype import Youtube
from mediaclass.imagetype import Image
from mediaclass.texttype import Text
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')
log.setLevel(logging.INFO)
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
        log.debug('New BADMedia class initializing...')

        # Base Directory
        self.appdir = os.path.dirname(os.path.realpath(__file__))
        self.jsondir = '%s/json/' % self.appdir
        self.webdir = '%s/../docs/' % self.appdir

        # Create class lists / html writer class instance
        self.htmls = Writer(dir=self.appdir)
        self.audios = []
        self.youtubes = []
        self.images = []
        self.texts = []

        self.load()
        return


    def load(self):
        log.debug('Loading BADMedia...')
        os.chdir(self.jsondir)

        # Load each JSON object from jsondir
        for file in os.listdir(self.jsondir):
            with open(file, 'r') as f:
                jso = json.loads(f.read())

            # Create appropriate class instance
            if jso['type'] == 'audio':
                media = Audio(dir=self.appdir, filename=file)
                self.audios.append(media)
            elif jso['type'] == 'image':
                media = Image(dir=self.appdir, filename=file)
                self.images.append(media)
            elif jso['type'] == 'text':
                media = Text(dir=self.appdir, filename=file)
                self.texts.append(media)
            elif jso['type'] == 'youtube':
                media = Youtube(dir=self.appdir, filename=file)
                self.youtubes.append(media)
            else:
                log.warning('%s is not properly formatted' % str(file))
        return


    def listMedia(self):
        log.debug('BADMedia.listMedia started...')

        for item in self.audios:
            print('%s\n' % item.name)
        for item in self.texts:
            print('%s\n' % item.name)
        for item in self.youtubes:
            print('%s\n' % item.name)
        for item in self.images:
            print('%s\n' % item.name)
        return


    def addMedia(self):
        log.debug('BADMedia.addMedia started...')

        answer = str(input('What type of media?\n\
            audio: an podcast or other audio stream\n\
            youtube: a youtube channel\n\
            image: an image feed\n\
            text: a text article feed\n\
            back: back to menu.\n'))

        if answer == 'audio':
            media = Audio(dir=self.appdir)
            self.audios.append(media)
        elif answer == 'youtube':
            media = YouTube(dir=self.appdir)
            self.youtubes.append(media)
        elif answer == 'image':
            media = Image(dir=self.appdir)
            self.images.append(media)
        elif answer == 'text':
            media = Text(dir=self.appdir)
            self.texts.append(media)
        elif answer == 'back':
            self.menu()
        else:
            print('Input invalid!')
            self.addMedia()
        return


    def clear(self, name):
        log.debug('BADMedia.clear started...')
        #TODO
        return


    def clearAll(self):
        log.debug('BADMedia.clearAll started...')

        for item in self.audios:
            item.clearJSON()
        for item in self.images:
            item.clearJSON()
        for item in self.youtubes:
            item.clearJSON()
        for item in self.texts:
            item.clearJSON()
        return


    def generatePage(self):
        log.debug('BADMedia.generatePage started...')
        #TODO
        return


    def menu(self):
        log.debug('BADMedia.menu started:')
        os.chdir(self.appdir)

        inp = ''
        inp = str(input('What would you like to do?\n\
        add: add new media source\n\
        clear: remove a media source\n\
        clearall: clear all media sources\n\
        create: generate webpage\n\
        exit: exit.\n'))

        if inp == 'add':
            self.addMedia()

        elif inp == 'clear':
            self.clear()

        elif inp == 'clearall':
            self.clearAll()

        elif inp == 'create':
            self.generatePage()

        elif inp == 'test':     # Placeholder for testing features
            self.load()

        else:
            print('Input invalid!')
            self.menu()
        return



if __name__ == '__main__':
    log.info('app.py started:')

    try:
        bad = BADMedia()
        bad.menu()

    except Exception:
        log.exception('Error in main process')
