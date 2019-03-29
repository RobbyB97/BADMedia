"""

    Author: Robby Bergers

    This is the class used to handle libsyn podcasts

"""

# External Libraries
import os
from bs4 import BeautifulSoup as bs
import json
import logging
import requests
import time
from libpyn.podcast import Podcast
