"""

    Author: Robby Bergers

    This is the class used to handle audio type media

"""

# External Libraries
import os
import json
import logging

# Internal Libraries
from mediaclass.media import Media

# Set Logger
log = logging.getLogger('BADMedia')



class Image(Media):


    def __init__(self, dir, filename = None):

        # Set media type and pass to Media class
        self.type = 'image'

        if filename:
            Media.__init__(self, dir=dir, filename=filename)
        else:
            Media.__init__(self, dir=dir)
        return
