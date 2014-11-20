#! /usr/bin/python
import sys
sys.path.append('../../')

print 'a' or 'b'

print '' or 'b'

print 'a' or 'b' or 'c'

print '' or [] or {}

def sidefx():
    """"""
    print 'in sidefx'
    return 1

print 'a' or sidefx()
    
