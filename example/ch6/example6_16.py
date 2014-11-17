#! /usr/bin/python

import os

print os.path.join("/home/vagrant//ap//", "xx.mp3")

print os.path.expanduser("~")

print os.path.join(os.path.expanduser("~"), "Python")
