#! /usr/bin/python

from xml.dom import minidom

xmldoc = minidom.parse('../../kgp/russiansample.xml')

title = xmldoc.getElementsByTagName('title')[0].firstChild.data

print title

convertedtitle = title.encode('koi8-r')

print convertedtitle
