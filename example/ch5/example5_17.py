#! /usr/bin/python

import sys
sys.path.append('../../')
import fileinfo

print fileinfo.MP3FileInfo

print fileinfo.MP3FileInfo.tagDataMap

m = fileinfo.MP3FileInfo()

print m.tagDataMap

