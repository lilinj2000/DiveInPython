#! /usr/bin/python

import re

print re.search('[^aeiou]y$', 'vacancy')

print re.search('[^aeiou]y$', 'boy')

print re.search('[^aeiou]y$', 'day')

print re.search('[^aeiou]y$', 'pita')
