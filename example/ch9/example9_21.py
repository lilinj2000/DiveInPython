#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

reflist = xmldoc.getElementsByTagName('ref')

print reflist

print reflist[0].toxml()

print reflist[1].toxml()
