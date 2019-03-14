"""

    Author: Robby Bergers

    This class is responsible for gathering instances of other media
    classes and generating a webpage from them.

"""

# External Libraries
import os
import logging

# Set Logger
log = logging.getLogger('BADMedia')



class Writer:


    def __init__(self, dir):
        log.debug('Initializing Writer class...')

        # Load base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        self.templates = {}     # Dictionary containing HTML templates

        # Methods to run on init
        self.loadMedia()
        self.getTemplates()
        return


    def loadMedia(self, audios = None, youtubes = None, texts = None, images = None):
        log.debug('Writer.loadMedia started...')

    	# Set lists of media objects
        if audios:
    	    self.audio = audios
        if youtubes:
            self.youtube = youtubes
        if texts:
    	    self.text = texts
        if images:
    	    self.image = images
        return


    def getTemplates(self):
        log.debug('Writer.getWraps started...')

        # Wrapper dictionary and keys
        self.mediawraps = {}
        types = ['audio', 'text', 'image', 'youtube']

        # Get wrap for each media type and add to dictionary
        for type in types:
            try:        # Open type wrap template, if it exists
                os.chdir(self.webdir)
                with open('./assets/templates/%s/wrap.html' % type, 'r') as f:
                    self.mediawraps[type] = f.read().split('|')
            except:
                log.exception('Could not find %s wrap template...' % type)
        return


    def updateMedia(self):
        log.debug('Writer.updateMedia started...')

        # Iterate through media lists and update JSON objects
        for item in self.audio:
            item.updateJSON()
        for item in self.youtube:
            item.updateJSON()
        for item in self.text:
            item.updateJSON()
        for item in self.image:
            item.updateJSON()
        return


    def writeSection(self):
        log.debug('Writer.writeSection started...')
        #TODO
        return
