#! /usr/bin/python

import sys
sys.path.append('../../')

from apihelper import info

import odbchelper

info(odbchelper)

print '=========================='

info(odbchelper, 30)

print '========================='

info(odbchelper, 30, 0)
