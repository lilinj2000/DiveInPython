#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

plist = xmldoc.getElementsByTagName('p')

print plist

print plist[0].toxml()

print plist[1].toxml()

print plist[2].toxml()
