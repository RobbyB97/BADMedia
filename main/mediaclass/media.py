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

# Internal Libraries
import audiotype
import imagetype
import texttype
import youtubetype
