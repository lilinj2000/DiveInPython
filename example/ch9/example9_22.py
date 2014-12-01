#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

reflist = xmldoc.getElementsByTagName('ref')

print reflist

firstref = reflist[0]

print firstref.toxml()

plist = firstref.getElementsByTagName('p')

print plist

print plist[0].toxml()

print plist[1].toxml()
