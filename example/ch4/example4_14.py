#! /usr/bin/python
import sys
sys.path.append('../../')

li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print li

print [elem for elem in li if len(elem)>1 ]

print [elem for elem in li if li.count(elem)==1]
       



