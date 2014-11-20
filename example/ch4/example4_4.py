#! /usr/bin/python

import sys
sys.path.append('../../')

from apihelper import info

import odbchelper

info(odbchelper)
print '=========================='

info(odbchelper, 12)
print '========================='

info(odbchelper, collapse=0)
print '========================='

info(spacing=15, object=odbchelper)
