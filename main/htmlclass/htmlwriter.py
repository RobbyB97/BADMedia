"""

    Author: Robby Bergers

    This class is responsible for gathering instances of other media classes and generating a webpage from them

"""

# External Libraries
import os
import logging

# Set Logger
log = logging.getLogger('BADMedia')



class Writer:
    def __init__(self, dir):
        self.appdir = dir
        self.jsondir = '%s/json/' % dir
        self.webdir = '%s/../docs/' % dir
