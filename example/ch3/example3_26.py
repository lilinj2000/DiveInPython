#! /usr/bin/python

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

print params.items()

print [k for k, v in params.items()]

print [v for k, v in params.items()]

print ["%s=%s" % (k, v) for k, v in params.items()]
