"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

import os
import app
import jsonhandler
import json
import logging

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

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

class Image:
    def __init__(self, filename):
        self.jsonobject = json.loads('%s%s.json' % (jsondir, filename))
        self.name = self.jsonobject['name']
        self.media = self.jsonobject['media']
