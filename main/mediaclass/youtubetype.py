"""

    Author: Robby Bergers

    This is the class used to handle youtube type media

"""

# External Libraries
import os
import json
import logging
from yt_iframe import yt

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Youtube(Media):


    def __init__(self, dir, filename = None):

        # Set media type and pass to Media class
        self.type = 'youtube'

        # Load JSON object (if filename argument passed)
        if filename:
            try:
                os.chdir(self.dir['json'])
                with open(filename, 'r') as f:
                    self.jsonobject = json.loads(f.read())
            except:
                log.warning('Error loading %s.json. Creating new media source...' % filename)
                self.getInfo()

            # Assign class attributes from JSON object
            self.name = self.jsonobject['name']
            self.link = self.jsonobject['xml']
            self.media = self.jsonobject['media']

        else:
            self.getInfo()
        return


    def getInfo(self):
        log.debug('Youtube.getInfo started...')

        # Get information from user
        self.name = str(input('What is the name of the Youtube channel?'))
        self.link = str(input('Enter the link to the channel:'))

        self.updateJSON()
        return


    def updateJSON(self):
        log.debug('%s.updateJSON started...' % self.name)

        self.getMedia()     # Refresh post entries

        # Construct dictionary
        masterdict = {}     # Final JSON object
        masterdict['type'] = self.type
        masterdict['name'] = self.name
        masterdict['xml'] = self.link
        masterdict['media'] = self.media

        # Store in json file
        os.chdir(self.dir['json'])
        jsonfile = open('%s.json' % self.name, 'w+')
        json_str = json.dumps(masterdict, sort_keys=True, indent=4)
        jsonfile.write(json_str)
        jsonfile.close()
        return


    def getMedia(self):
        log.debug('%s.getMedia started...' % self.name)

        self.media = {}     # Reset media dictionary

        i=0 # Keys for dict
        try:
            for element in yt.channel(self.link)
                self.media[str(i)] = element
                i += 1
        except:
            log.warning('%s.getMedia Error! Link not valid')
            self.getInfo()
        return
