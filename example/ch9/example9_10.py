#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

grammarNode = xmldoc.childNodes[1]

print grammarNode.toxml()
