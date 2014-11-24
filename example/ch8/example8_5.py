#! /usr/bin/python

import urllib

sock = urllib.urlopen("http://diveintopython.org/")

htmlSource = sock.read()

sock.close()

print htmlSource
