#! /usr/bin/python

# roman digit, verify the tens(10) digit

# roman digit:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# for the 10 digit
# 10 = X
# 20 = XX
# 30 = XXX
# 40 = XL
# 50 = L
# 60 = LX
# 70 = LXX
# 80 = LXXX
# 90 = XM

import re

pattern = '^M?M?M?(CD|CM|D?C?C?C?)(XM|XL|L?X?X?X?)$'

t1 = re.search(pattern, 'MCMXL')  # 1940
print t1

t2 = re.search(pattern, 'MCML')   # 1950
print t2

t3 = re.search(pattern, 'MCMLX') # 1960
print t3

t4 = re.search(pattern, 'MCMLXXX') # 1980
print t4

t41 = re.search(pattern, 'MCMLXXXX') # none
print t41


t5 = re.search(pattern, '')
print t5


