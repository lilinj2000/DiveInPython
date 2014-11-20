#! /usr/bin/python

d = {"server":"mpilgrim", "database":"master"}

d["retrycount"] = 3

d[42] = "douglas"
print d

del d[42]
print d

d.clear()
print d
