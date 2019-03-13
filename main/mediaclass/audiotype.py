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

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Audio(Media):


    def __init__(self, dir, filename = None):

        # Set media type and pass to Media class
        self.type = 'audio'

        if filename:
            Media.__init__(self, dir=dir, filename=filename)
        else:
            Media.__init__(self, dir=dir)
        return
