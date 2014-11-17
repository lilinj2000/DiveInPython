#! /usr/bin/python

# 800-555-1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234

import re

phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$');

t1 = phonePattern.search('800-555-1212-1234').groups()
print t1

t1 = phonePattern.search('800 555 1212 1234').groups()
print t1

t1 = phonePattern.search('80055512121234')
print t1

t1 = phonePattern.search('800-555-1212')
print t1
