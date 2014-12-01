#!/usr/bin/python

import urllib

from xml.dom import minidom

contents = '''
<?xml version="1.0" ?><note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'''

import StringIO

ssock = StringIO.StringIO(contents)
print ssock.read()
print ssock.read()
# print ssock.read()
# print ssock.read()
# print ssock.read()

ssock.seek(0)
print ssock.read(15)
print ssock.read(15)
print ssock.read()

ssock.close()

