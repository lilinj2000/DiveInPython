#!/usr/bin/python

import urllib

from xml.dom import minidom

contents = '''<?xml version="1.0" ?><note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'''

xmldoc = minidom.parseString(contents)


print xmldoc.toxml()
