#! /usr/bin/python

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

print "%(pwd)s" % params

print "%(pwd)s is not a good password for %(uid)s" % params

print "%(database)s of mind, %(database)s of body" % params
