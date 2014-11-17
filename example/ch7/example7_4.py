#! /usr/bin/python

# roman digit, verify the hundreds(100) digit

# roman digit:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# for the 100 digit
# 100 = C
# 200 = CC
# 300 = CCC
# 400 = CD
# 500 = D
# 600 = DC
# 700 = DCC
# 800 = DCCC
# 900 = CM

import re

pattern = '^M?M?M?(CD|CM|D?C?C?C?)$'

t1 = re.search(pattern, 'MCM')  # 1900
print t1

t2 = re.search(pattern, 'MD')   # 1500
print t2

t3 = re.search(pattern, 'MMMCCC') # 3300
print t3

t4 = re.search(pattern, 'MCMC') # none
print t4

t5 = re.search(pattern, '')
print t5


