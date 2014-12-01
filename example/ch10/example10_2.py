#!/usr/bin/python

import urllib

from xml.dom import minidom

# <?xml version="1.0" ?><note>
#   <to>Tove</to>
#   <from>Jani</from>
#   <heading>Reminder</heading>
#   <body>Don't forget me this weekend!</body>
# </note>
usock = urllib.urlopen('http://www.xmlfiles.com/examples/note.xml')

xmldoc = minidom.parse(usock)

usock.close()

print xmldoc.toxml()
