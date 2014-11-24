#! /usr/bin/python

import sys
sys.path.append('../../')

import fileinfo

f = fileinfo.FileInfo('example5_7.py')

print f.__class__

print f.__doc__

print f
