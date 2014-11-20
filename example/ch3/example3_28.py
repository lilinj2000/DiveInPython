#! /usr/bin/python

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

li = ["%s=%s" % (k, v) for k, v in params.items()]
print li

s = ";".join(li)
print s

print s.split(";")

print s.split(";", 1)
