#! /usr/bin/python

import sys
sys.path.append('../../')
import fileinfo

mp3file = fileinfo.MP3FileInfo()

print mp3file

mp3file["name"] = "./example5_15.py"

print mp3file    

mp3file["name"] = "./example5_12.py"
print mp3file

