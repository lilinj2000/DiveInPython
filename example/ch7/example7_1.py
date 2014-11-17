#! /usr/bin/python

# match the word on the end of string

s = '100 NORTH MAIN ROAD'
s1 = s.replace('ROAD', 'RD.')
print 's1 ', s1

s = '100 NORTH BROAD ROAD'
s2 = s.replace('ROAD', 'RD.')
print 's2 ', s2

s3 = s[:-4] + s[-4:].replace('ROAD', 'RD.')
print 's3 ', s3

import re
s4 = re.sub('ROAD$', 'RD.', s)
print 's4 ', s4
