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

        if filename:    # If reference to json file exists
            try:
                self.jsonobject = json.loads('%s%s.json' % (self.jsondir, filename))
            except Exception:
                log.exception('Error loading %s.json. Creating new media source...')
                self.getInfo()
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']
            self.tag = self.jsonobject['tag']

        else:       # If this is a new media object
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
