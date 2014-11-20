#! /usr/bin/python
import sys
sys.path.append('../../')

import string
print string.punctuation

print string.join

print callable(string.punctuation)

print callable(string.join)

print string.join.__doc__

