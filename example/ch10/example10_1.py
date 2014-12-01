#!/usr/bin/python

from xml.dom import minidom

fsock = open('../../kgp/binary.xml')

xmldoc = minidom.parse(fsock)

fsock.close()

print xmldoc.toxml()
