"""

    Author: Robby Bergers

    This is the master class for all media types

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests


# Set Logger
log = logging.getLogger('BADMedia')



class Media:


    def __init__(self, dir, filename = None):
        log.info('New Media class initializing...')

        # Set base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        # Get HTML innerwrap
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/%s/post.html' % str(self.type), 'r') as f:
                self.innerwrap = f.read.split('|')
        except Exception:
            log.exception('Could not find %s innerwrap template...' % str(self.type))

        # Get HTML outerwrap
        try:
            os.chdir(self.webdir)
            with open('./assets/templates/%s/wrap.html' % str(self.type), 'r') as f:
                self.outerwrap = f.read.split('|')
        except Exception:
            log.exception('Could not find %s outerwrap template...' % str(self.type))

        # Load JSON object if filename argument passed
        if filename:
            try:
                os.chdir(self.jsondir)
                with open(filename, 'r') as f:
                    self.jsonobject = json.loads(f.read())
            except:
                log.warning('Error loading %s.json. Creating new media source...' % filename)
                self.getInfo()
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']
            self.tag = self.jsonobject['tag']

        # Get information to create media object if filename argument not passed
        if not filename:
            self.getInfo()

        return


    def getInfo(self):
        log.info('Media.getInfo started')

        # Get media information from user
        self.name = str(input('What should this media be called?\n'))
        self.link = str(input('Enter the link to the feed:\n'))
        self.tag = str(input('Enter tag name containing media: [default = \'enclosure\']'))
        if not self.tag:
            self.tag = 'enclosure'
        self.updateJSON()


    def getMedia(self):
        log.info('%s.getMedia started...' % self.name)

        self.media = {}     # Reset list of audio links

        # Get XML file
        try:
            xml = requests.get(self.link).text
        except Exception:
            log.exception('Error loading XML from %s...' % self.link)

        # Parse and scrape audio file links
        soup = bs(xml, "lxml")
        i=0 # Counter, serves as ID for each entry
        for element in soup.findAll(self.tag):
            self.media[str(i)] = element['url']
            i += 1
        log.info('Found %s files in XML...' % str(len(self.media)))
        return


    def updateJSON(self):
        log.info('%s.updateJSON started...' % self.name)

        self.getMedia()     # Refresh post entries

        # Construct dictionary
        masterdict = {}     # Final JSON object
        masterdict['type'] = self.type
        masterdict['name'] = self.name
        masterdict['xml'] = self.link
        masterdict['tag'] = self.tag
        masterdict['media'] = self.media

        # Store in json file
        os.chdir(self.jsondir)
        jsonfile = open('%s.json' % self.name, 'w+')
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        jsonfile.write(json_str)
        jsonfile.close()
        return


    def clearJSON(self):
        log.info('%s.clearJSON started...' % self.name)

        # Remove class instances' JSON file if it exists
        os.chdir(self.jsondir)
        try:
            os.remove('%s.json' % self.name)
        except:
            log.warning('%s.json doesn\'t exist.' % self.name)
        return
