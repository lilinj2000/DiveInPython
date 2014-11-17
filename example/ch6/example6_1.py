#! /usr/bin/python

try:
    fsock = open("/notthere", "r")
except IOError:
    print "The file does not exist, exitting gracefully"

print "This line will always print"
