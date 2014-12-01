#!/usr/bin/python

import urllib

from xml.dom import minidom

contents = '''<?xml version="1.0" ?><note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'''

import StringIO

ssock = StringIO.StringIO(contents)

# print ssock.read()

xmldoc = minidom.parse(ssock)

ssock.close()

print xmldoc.toxml()
