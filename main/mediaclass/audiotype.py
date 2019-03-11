"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
import app
import json
import logging

# Set Logger
log = logging.getLogger('BADMedia')
log.setLevel(logging.WARNING)
handlerpath = appdir + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)



class Audio:
    def __init__(self, dir, filename = None):
        self.appdir = dir
        self.jsondir = '%s/json/' % appdir
        self.webdir = '%s/../docs/' % appdir
        if filename != None:
            self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
            self.name = self.jsonobject['name']
            self.media = self.jsonobject['media']
