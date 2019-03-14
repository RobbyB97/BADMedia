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

        # Initialize template dictionaries
        self.master = {}        # HTML Header / Footer / Navbar
        self.audio = {}
        self.image = {}
        self.text = {}
        self.youtube = {}

        # Methods to run on init
        self.loadMedia()
        self.getTemplates()
        return


    def loadMedia(self, audios = None, youtubes = None, texts = None, images = None):
        log.debug('Writer.loadMedia started...')

    	# Set lists of media objects
    	self.audiolist = audios
        self.youtubelist = youtubes
        self.textlist = texts
        self.imagelist = images
        return


    def getTemplates(self):
        log.debug('Writer.getWraps started...')

        try:        # Get audio templates
            os.chdir(self.webdir)
            with open('./assets/templates/audio/wrap.html', 'r') as f:
                self.audio['outer'] = f.read().split('|')
            with open('./assets/templates/audio/post.html', 'r') as f:
                self.audio['inner'] = f.read().split('|')
        except:
            log.exception('Could not find audio template...')

        try:        # Get image templates
            os.chdir(self.webdir)
            with open('./assets/templates/image/wrap.html', 'r') as f:
                self.image['outer'] = f.read().split('|')
            with open('./assets/templates/image/post.html', 'r') as f:
                self.image['inner'] = f.read().split('|')
        except:
            log.exception('Could not find image template...')

        try:        # Get youtube templates
            os.chdir(self.webdir)
            with open('./assets/templates/youtube/wrap.html', 'r') as f:
                self.youtube['outer'] = f.read().split('|')
            with open('./assets/templates/youtube/post.html', 'r') as f:
                self.youtube['inner'] = f.read().split('|')
        except:
            log.exception('Could not find youtube template...')

        try:        # Get text templates
            os.chdir(self.webdir)
            with open('./assets/templates/text/wrap.html', 'r') as f:
                self.text['outer'] = f.read().split('|')
            with open('./assets/templates/text/post.html', 'r') as f:
                self.text['inner'] = f.read().split('|')
        except:
            log.exception('Could not find text template...')
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
