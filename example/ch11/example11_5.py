#!/usr/bin/python

# import httplib

# httplib.HTTPConnection.debuglevel = 1

import urllib2

h = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(h)
# urllib2.install_opener(opener)
# data = urllib2.urlopen('http://diveintomark.org/xml/atom.xml').read()

# print data

request = urllib2.Request('http://diveintomark.org/xml/atom.xml')

print request

print request.get_full_url()

request.add_header('User-Agent', 'OpenAnything/1.0 +http://diveintopython.org/')
# opener = urllib2.build_opener()
feeddata = opener.open(request).read()

print feeddata
