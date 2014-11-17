#! /usr/bin/python

# verify the roman digit, format {n,m}

# roman digit:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000


import re

pattern = '^(M{0,3})(CD|CM|D?C{0,3})(XM|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

t1 = re.search(pattern, 'MDLV')  # 1555
print t1

t2 = re.search(pattern, 'MMDCLXVI')   # 2666
print t2

t3 = re.search(pattern, 'MMMDCCCLXXXVIII') # 3888
print t3

t4 = re.search(pattern, 'I') # 1
print t4

t5 = re.search(pattern, '')
print t5


