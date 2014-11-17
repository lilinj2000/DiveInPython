#! /usr/bin/python

import sys

from ssl import SSLError
print SSLError.__module__

print sys.modules[SSLError.__module__]
