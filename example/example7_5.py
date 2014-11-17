#! /usr/bin/python

# roman digit, verify the thousands(1000) digit, format {n, m}

# roman digit:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

import re

pattern = '^M?M?M?$'

t1 = re.search(pattern, 'M')
print t1

t2 = re.search(pattern, 'MM')
print t2

t3 = re.search(pattern, 'MMM')
print t3

t4 = re.search(pattern, 'MMMM')
print t4

t5 = re.search(pattern, '')
print t5


