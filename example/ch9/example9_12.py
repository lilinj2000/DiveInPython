#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

grammarNode = xmldoc.childNodes[1]
print grammarNode

refNode = grammarNode.childNodes[1]
print refNode

print refNode.childNodes

pNode = refNode.childNodes[1]
print pNode

print pNode.toxml()

print pNode.firstChild

print pNode.firstChild.data

