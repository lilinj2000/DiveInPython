#!/usr/bin/python

import urllib2

data = urllib2.urlopen('http://diveintomark.org/xml/atom.xml').read()

print data
