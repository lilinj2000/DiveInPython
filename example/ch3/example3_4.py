#! /usr/bin/python

d = {"server":"mpilgrim", "database":"master"}
print d

d["retrycount"] = 3
print d

d[42] = "douglas"
print d
