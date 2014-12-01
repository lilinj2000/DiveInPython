#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/binary.xml')

reflist = xmldoc.getElementsByTagName('ref')

bitref = reflist[0]

a = bitref.attributes['id']

print a

print a.name

print a.value
