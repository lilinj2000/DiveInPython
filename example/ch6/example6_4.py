#! /usr/bin/python

f = open("example6_1.py", "rb")

print f

print f.tell()

f.seek(-128, 2)

print f.tell()

data = f.read(128)

print data[-20:]

print f.tell()
