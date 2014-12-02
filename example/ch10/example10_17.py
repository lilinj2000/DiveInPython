#!/usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/kant.xml')

print xmldoc

print xmldoc.__class__

print xmldoc.__class__.__name__

