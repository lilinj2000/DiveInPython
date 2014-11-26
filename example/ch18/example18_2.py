#! /usr/bin/python

import timeit

t = timeit.Timer("sys.path", "import sys")

print t.timeit()

print t.repeat(3, 2000000)


    

