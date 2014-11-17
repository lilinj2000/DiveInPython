#! /usr/bin/python

import os

print os.path.split("/home/vagrant//ap//xx.mp3")

(filepath, filename) = os.path.split("/home/vagrant//ap//xx.mp3")

print filepath

print filename

(shortname, extension) = os.path.splitext(filename)

print shortname

print extension

