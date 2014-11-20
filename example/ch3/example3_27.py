#! /usr/bin/python

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

print ["%s=%s" % (k, v) for k, v in params.items()]

print ";".join(["%s=%s" % (k, v) for k, v in params.items()])
