#! /usr/bin/python

f = open("example6_1.py", "rb")

print f

f.close()

print f

print f.closed

try:
    f.seek(0)
except ValueError:
    print "ValueError on f.seek()"

try:
    f.tell()
except ValueError:
    print "ValueError on f.tell()"

try:
    f.read()
except ValueError:
    print "ValueError on f.read()"

f.close()

print f.closed
