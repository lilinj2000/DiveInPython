#! /usr/bin/python

logfile = open('test.log', 'w')
logfile.write('test succeeded')
logfile.close()

print file('test.log').read()

logfile = open('test.log', 'a')
logfile.write('line 2')
logfile.close()

print file('test.log').read()