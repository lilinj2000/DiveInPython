#!/usr/bin/python

import os, re

files = os.listdir(os.getcwd())

test = re.compile("test\.py$", re.IGNORECASE)

files = [f for f in files if test.search(f)]

print files
