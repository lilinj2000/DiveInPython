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

pattern = """
^                               # beginning of string
(M{0,3})                        #  thousands - 0 to 3 M's
(CD|CM|D?C{0,3})                # hundreds - 900 (CM), 400 (CD), 
                                # 0-300 (0 to 3 C's)         
                                # or 500-800 (D, followed by 0 to 3 C's)
(XM|XL|L?X{0,3})                # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                                # or 50-80 (L, followed by 0 to 3 X's)
(IX|IV|V?I{0,3})                # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                                # or 5-8 (V, followed by 0 to 3 I's)
$                               #  end of string
"""

t1 = re.search(pattern, 'MDLV', re.VERBOSE)  # 1555
print t1

t2 = re.search(pattern, 'MMDCLXVI', re.VERBOSE)   # 2666
print t2

t3 = re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE) # 3888
print t3

t4 = re.search(pattern, 'I', re.VERBOSE) # 1
print t4

t5 = re.search(pattern, '', re.VERBOSE)
print t5


