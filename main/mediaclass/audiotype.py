"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests

# Set Logger
log = logging.getLogger('BADMedia')


class Audio:


    def __init__(self, dir, filename = None):

        # Set base project directories
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir

        if filename:    # If reference to json file exists
            self.jsonobject = json.loads('%s%s.json' % (self.jsondir, filename))
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']
            self.tag = self.jsonobject['tag']

        else:       # If this is a new media object
            self.getInfo()
        return


    def getInfo(self):

        # Get object information from user
        self.type = 'audio'
        self.name = str(input('What should this media be called?\n'))
        self.link = str(input('Enter the link to the feed:\n'))
        self.tag = str(input('Enter tag name containing media: [default = \'enclosure\']'))
        if not self.tag:
            self.tag = 'enclosure'

        self.saveToJSON()
        return


    def getMedia(self):

        self.media = {}     # Reset list of audio links

        # Update list of media links from RSS feed
        xml = requests.get(self.link).text
        soup = bs(xml, "lxml")
        i=0 # Counter, serves as ID for each entry
        for element in soup.findAll(self.tag):
            self.media[str(i)] = element['url']
            i += 1
        return


    def saveToJSON(self):

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
        jsonfile = open('./json/%s.json' % self.name, 'w')
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        jsonfile.write(json_str)
        jsonfile.close()
