#!/usr/bin/python

# import httplib

# httplib.HTTPConnection.debuglevel = 1

import urllib2, sys

sys.path.append('../..')
import openanything

# h = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(openanything.DefaultErrorHandler())
# urllib2.install_opener(opener)
# data = urllib2.urlopen('http://diveintomark.org/xml/atom.xml').read()

# print data

request = urllib2.Request('http://sina.com.cn')

# opener = urllib2.build_opener()
firstdatastream = opener.open(request)

print firstdatastream.headers.dict

request.add_header('If-Modified-Since', firstdatastream.headers.get('Last-Modified'))

seconddatastream = opener.open(request)

print seconddatastream.status

print seconddatastream.read()
