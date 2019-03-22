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
        self.dir = {}
        self.dir['app'] = os.path.dirname(os.path.realpath(__file__))
        self.dir['json'] = '%s/json/' % self.dir['app']
        self.dir['web'] = '%s/../docs/' % self.dir['app']

        # Ensure JSON directory exists
        if not os.path.exists(self.dir['json']):
            log.warning('JSON directory not detected. Creating...')
            os.makedirs(self.dir['json'])

        # Create Writer class/ Media class lists and populate them
        self.writer = Writer(dir=self.dir)
        self.audios = []
        self.youtubes = []
        self.images = []
        self.texts = []
        self.loadMedia()
        return


    def loadMedia(self):
        log.debug('Loading BADMedia...')
        os.chdir(self.dir['json'])

        # Load each JSON object from dir['json']
        for file in os.listdir(self.dir['json']):
            log.info('Loading %s...' % file)
            with open(file, 'r') as f:
                jso = json.loads(f.read())

            # Create appropriate class instance
            if jso['type'] == 'audio':
                media = Audio(dir=self.dir, filename=file)
                self.audios.append(media)
            elif jso['type'] == 'image':
                media = Image(dir=self.dir, filename=file)
                self.images.append(media)
            elif jso['type'] == 'text':
                media = Text(dir=self.dir, filename=file)
                self.texts.append(media)
            elif jso['type'] == 'youtube':
                media = Youtube(dir=self.dir, filename=file)
                self.youtubes.append(media)
            else:
                log.warning('%s is not properly formatted' % str(file))

        # Update Media class lists in Writer class
        self.writer.loadMedia(audios=self.audios, youtubes=self.youtubes, texts=self.texts, images=self.images)
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

        # Menu
        answer = str(input('What type of media?\n\
            audio: an podcast or other audio stream\n\
            youtube: a youtube channel\n\
            image: an image feed\n\
            text: a text article feed\n\
            back: back to menu.\n'))

        # Menu Options
        if answer == 'audio':
            media = Audio(dir=self.dir)
            self.audios.append(media)
            self.writer.updateMedia()

        elif answer == 'youtube':
            media = Youtube(dir=self.dir)
            self.youtubes.append(media)
            self.writer.updateMedia()

        elif answer == 'image':
            media = Image(dir=self.dir)
            self.images.append(media)
            self.writer.updateMedia()

        elif answer == 'text':
            media = Text(dir=self.dir)
            self.texts.append(media)
            self.writer.updateMedia()

        elif answer == 'back':
            self.menu()

        else:
            print('Input invalid!')
            self.addMedia()
        return


    def clear(self, name=None):
        log.debug('BADMedia.clear started...')

        if not name:    # Get name of object if none was given
            name = str(input('Enter the name of the media:'))

        found = False   # Flag

        # Loop through media list until match is found
        while not found:
            for item in self.audios:
                if item.name == name:
                    log.info('%s found. Clearing...' % name)
                    item.clearJSON()
                    self.writer.updateMedia()
                    found = True
            for item in self.youtubes:
                if item.name == name:
                    log.info('%s found. Clearing...' % name)
                    item.clearJSON()
                    self.writer.updateMedia()
                    found = True
            for item in self.images:
                if item.name == name:
                    log.info('%s found. Clearing...' % name)
                    item.clearJSON()
                    self.writer.updateMedia()
                    found = True
            for item in self.texts:
                if item.name == name:
                    log.info('%s found. Clearing...' % name)
                    item.clearJSON()
                    self.writer.updateMedia()
                    found = True
            break

        if not found:
            log.warning('%s does not match any media object...' % name)
            self.menu()
        return


    def clearAll(self):
        log.debug('BADMedia.clearAll started...')

        # Clear JSON files
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

        self.writer.compileWebpage()
        return


    def menu(self):
        log.debug('BADMedia.menu started:')
        os.chdir(self.dir['app'])

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

        elif inp == 'exit':
            return

        elif inp == 'test':     # Placeholder for testing features
            for element in self.audios:
                element.updateJSON()

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
