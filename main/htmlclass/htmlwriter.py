"""

    Author: Robby Bergers

    This class is responsible for gathering instances of other media classes
    and generating a webpage from them

"""

# External Libraries
import os

# Set Logger
log = logging.getLogger('BADMedia')

# Base Directory
appdir = os.path.dirname(os.path.realpath(__file__))
jsondir = '%s/json/' % appdir
webdir = '%s/../docs/' % appdir

class Writer:
    def __init__(self):
        self.path  = webdir
