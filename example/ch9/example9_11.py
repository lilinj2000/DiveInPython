#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

grammarNode = xmldoc.childNodes[1]

print grammarNode.childNodes

print grammarNode.firstChild.toxml()

print grammarNode.childNodes[1].toxml()

print grammarNode.childNodes[3].toxml()

print grammarNode.lastChild.toxml()

