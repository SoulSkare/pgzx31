#!/usr/bin/env python3

import os
import re
import sys
from argparse import ArgumentParser
from time import sleep
from shutil import copyfile

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Referer': 'https://ustv247.tv/watch-abc-live-stream/'}


url = 'https://ustv247.tv/clappr.php?stream=AMC'
r = requests.get(url, allow_redirects=True, headers=headers)

open('AMC.txt', 'wb').write(r.content)

