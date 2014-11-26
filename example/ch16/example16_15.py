#!/usr/bin/python

moduleNames = ['sys', 'os', 're', 'unittest']

print moduleNames

modules = map(__import__, moduleNames)

print modules

print modules[0].version

import sys

print sys.version
