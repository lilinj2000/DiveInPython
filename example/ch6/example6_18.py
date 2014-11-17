#! /usr/bin/python

import os

print os.listdir("/home/vagrant")

dirname = "/home/vagrant"

print os.listdir(dirname)

t = [ f for f in os.listdir(dirname)
  if os.path.isfile(os.path.join(dirname, f))]

print t



