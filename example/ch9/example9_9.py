#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

print xmldoc.childNodes

print xmldoc.childNodes[0]

print xmldoc.firstChild
