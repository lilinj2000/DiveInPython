#! /usr/bin/python

import sys
sys.path.append('../../')
import fileinfo

def leakmem():
    """"""
    f = fileinfo.FileInfo('example5_7.py')

for i in range(100):
    leakmem()
