#! /usr/bin/python

import re

print re.sub('y$', 'ies', 'vacancy')

print re.sub('y$', 'ies', 'agency')

print re.sub('([^aeiou])y$', r'\1ies', 'vacancy')
