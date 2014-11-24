#! /usr/bin/python

import sys
sys.path.append('../../')
import fileinfo

def __gettime__(self, key):
    """"""
    return self.data[key]

def __settime__(self, key, item):
    """"""
    self.data[key] = item
    
f = fileinfo.FileInfo('./example5_13.py')
print f

f.__setitem__("genre", 31)

print f

f["genre"] = 32

print f
