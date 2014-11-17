#! /usr/bin/python

try:
    f = open("notthere", "rb", 0)
    try:
        f.seek(-128, 2)
        data = f.read(128)
    finally:
        f.close()
except IOError:
    print 'the file not exist'
    pass


