#! /usr/bin/python

import sys
sys.path.append('../..')

import urllib, urllister

# usock = urllib.urlopen("http://diveintopython.org/")
usock = urllib.urlopen("http://sourceforge.net/")

parser = urllister.URLLister()

parser.feed(usock.read())

usock.close()
parser.close()

for url in parser.urls:
    print url

