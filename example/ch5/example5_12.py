#! /usr/bin/python

import sys
sys.path.append('../../')
import fileinfo

def __gettime__(self, key):
    """"""
    return self.data[key]

f = fileinfo.FileInfo('./example5_12.py')
print f

print f.__getitem__("name")

print f["name"]
