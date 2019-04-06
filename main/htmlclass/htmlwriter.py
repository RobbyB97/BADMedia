"""

    Author: Robby Bergers

    This class is responsible for gathering instances of other media
    classes and generating a webpage from them.

"""

# External Libraries
import os
import logging
from yt_iframe import yt

# Set Logger
log = logging.getLogger('BADMedia')



class Writer:


    def __init__(self, dir):
        log.debug('Initializing Writer class...')

        # Load base project directories
        self.dir = dir

        # Initialize template dictionaries
        self.master = {}        # HTML Header / Footer / Navbar
        self.audio = {}
        self.libsyn = {}
        self.image = {}
        self.text = {}
        self.youtube = {}

        # Initialize state booleans
        self.hasLibsyn = False
        self.hasAudio = False
        self.hasText = False
        self.hasImage = False
        self.hasYouTube = False

        # Methods to run on init
        self.getTemplates()
        return


    def loadMedia(self, audios=None, libsyns=None, youtubes=None, texts=None, images=None):
        log.debug('Writer.loadMedia started...')

        # Set lists of media objects
        if audios:
            self.hasAudio = True
            self.audiolist = audios
        else:
            self.audiolist = []

        if libsyns:
            self.hasLibsyn = True
            self.libsynlist = libsyns
        else:
            self.libsynlist = []

        if youtubes:
            self.hasYouTube = True
            self.youtubelist = youtubes
        else:
            self.youtubelist = []

        if texts:
            self.hasText = True
            self.textlist = texts
        else:
            self.textlist = []

        if images:
            self.hasImage = True
            self.imagelist = images
        else:
            self.imagelist = []
        return


    def getTemplates(self):
        log.debug('Writer.getWraps started...')

        try:        # Get master templates
            os.chdir(self.dir['web'])
            with open('./assets/templates/header.html', 'r') as f:
                self.master['header'] = f.read().split('|')
                self.master['header'].pop(0)
            with open('./assets/templates/topbar.html', 'r') as f:
                self.master['topbar'] = f.read().split('|')
                self.master['topbar'].pop(0)
            with open('./assets/templates/pages.html', 'r') as f:
                self.master['pages'] = f.read().split('|')
                self.master['pages'].pop(0)
        except:
            log.exception('Could not find master template...')

        try:        # Get audio templates
            os.chdir(self.dir['web'])
            with open('./assets/templates/audio/wrap.html', 'r') as f:
                self.audio['outer'] = f.read().split('|')
                self.audio['outer'].pop(0)
            with open('./assets/templates/audio/post.html', 'r') as f:
                self.audio['inner'] = f.read().split('|')
                self.audio['inner'].pop(0)
        except:
            log.exception('Could not find audio template...')

        try:        # Get libsyn post template
            os.chdir(self.dir['web'])
            with open('./assets/templates/libsyn/post.html', 'r') as f:
                self.libsyn['inner'] = f.read().split('|')
                self.libsyn['inner'].pop(0)
        except:
            log.exception('Could not find libsyn template...')

        try:        # Get image templates
            os.chdir(self.dir['web'])
            with open('./assets/templates/image/wrap.html', 'r') as f:
                self.image['outer'] = f.read().split('|')
                self.image['outer'].pop(0)
            with open('./assets/templates/image/post.html', 'r') as f:
                self.image['inner'] = f.read().split('|')
                self.image['inner'].pop(0)
        except:
            log.exception('Could not find image template...')

        try:        # Get youtube templates
            os.chdir(self.dir['web'])
            with open('./assets/templates/youtube/wrap.html', 'r') as f:
                self.youtube['outer'] = f.read().split('|')
                self.youtube['outer'].pop(0)
        except:
            log.exception('Could not find youtube template...')

        try:        # Get text templates
            os.chdir(self.dir['web'])
            with open('./assets/templates/text/wrap.html', 'r') as f:
                self.text['outer'] = f.read().split('|')
                self.text['outer'].pop(0)
            with open('./assets/templates/text/post.html', 'r') as f:
                self.text['inner'] = f.read().split('|')
                self.text['inner'].pop(0)
        except:
            log.exception('Could not find text template...')
        return


    def updateMedia(self):
        log.debug('Writer.updateMedia started...')

        # Iterate through media lists and update JSON objects
        for item in self.audiolist:
            item.updateJSON()
        for item in self.libsynlist:
            item.updateJSON()
        for item in self.youtubelist:
            item.updateJSON()
        for item in self.textlist:
            item.updateJSON()
        for item in self.imagelist:
            item.updateJSON()
        return


    def compileAudio(self):
        log.debug('Writer.compileAudio started...')
        #TODO: Make sure this compiles properly if only libsyn, or if only audio

        self.audiosection = []        # Declare/ Clear Audio HTML

        # Loop through Libsyn class instances
        for object in self.libsynlist:
            self.audiosection.append(self.audio['outer'][0])
            self.audiosection.append(object.name)
            self.audiosection.append(self.audio['outer'][1])

            # Loop through list of media links in each Libsyn class
            for media in object.media['iframes']:
                self.audiosection.append(self.libsyn['inner'][0])
                self.audiosection.append(object.media['iframes'][media])
                self.audiosection.append(self.libsyn['inner'][1])

        # Loop through Audio class instances
        for object in self.audiolist:
            self.audiosection.append(self.audio['outer'][0])
            self.audiosection.append(object.name)
            self.audiosection.append(self.audio['outer'][1])

            # Loop through list of media links in each Audio class
            for media in object.media:
                self.audiosection.append(self.audio['inner'][0])
                self.audiosection.append(media)
                self.audiosection.append(self.audio['inner'][1])
                self.audiosection.append(object.media[media])
                self.audiosection.append(self.audio['inner'][2])

        # Close audio section
        self.audiosection.append(self.audio['outer'][2])
        return


    def compileImage(self):
        log.debug('Writer.compileImage started...')

        self.imagesection = []        # Declare/ Clear Image HTML
        #TODO
        return


    def compileYoutube(self):
        log.debug('Writer.compileYoutube started...')

        self.youtubesection = []        # Declare/ Clear Youtube HTML

        # Loop through Youtube class instance
        for object in self.youtubelist:
            self.youtubesection.append(self.youtube['outer'][0])
            self.youtubesection.append(object.name)
            self.youtubesection.append(self.youtube['outer'][1])

            # Loop through media dictionary
            for media in object.media:
                vid = yt.video(object.media[media])
                self.youtubesection.append(vid)
                self.youtubesection.append('</br>')

        # Close Youtube section
        self.youtubesection.append(self.youtube['outer'][2])
        return


    def compileText(self):
        log.debug('Writer.compileText started...')

        self.textsection = []        # Declare/ Clear Text HTML
        #TODO
        return


    def compileWebpage(self):
        log.debug('Writer.compileWebpage started...')

        os.chdir(self.dir['web'])

        # Compile media sections
        self.compileAudio()
        self.compileImage()
        self.compileYoutube()
        self.compileText()

        # Generate HTML file
        with open('index.html', 'w') as f:
            f.write(self.master['header'][0])       # HTML head/meta

            # Write topbar
            f.write(self.master['topbar'][0])
            if self.hasAudio or self.hasLibsyn:
                f.write(self.master['topbar'][1])
            if self.hasImage:
                f.write(self.master['topbar'][2])
            if self.hasText:
                f.write(self.master['topbar'][3])
            if self.hasYouTube:
                f.write(self.master['topbar'][4])
            f.write(self.master['topbar'][5])

            f.write(self.master['pages'][0])

            if self.hasAudio or self.hasLibsyn:   # Write audio section
                f.write(self.master['pages'][1])
                for line in self.audiosection:
                    f.write(line)
                f.write(self.master['pages'][2])

            if self.hasYouTube:     # Write youtube section
                f.write(self.master['pages'][3])
                for line in self.youtubesection:
                    f.write(line)
                f.write(self.master['pages'][4])

            if self.hasImage:       # Write image section
                f.write(self.master['pages'][5])
                for line in self.imagesection:
                    f.write(line)
                f.write(self.master['pages'][6])

            if self.hasText:        # Write text section
                f.write(self.master['pages'][7])
                for line in self.textsection:
                    f.write(line)
                f.write(self.master['pages'][8])

            # Write closing tags/footer
            f.write(self.master['header'][1])

        #TODO
        return
