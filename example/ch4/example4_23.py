#! /usr/bin/python
import sys
sys.path.append('../../')

def foo():
    print 2

foo()

print foo.__doc__

print foo.__doc__==None

print str(foo.__doc__)
    
