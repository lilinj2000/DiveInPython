#! /usr/bin/python

def flib(n):
    """"""
    print 'n=', n
    if n>1:
        return n*flib(n-1)
    else:
        print 'end of the line'
        return 1

if __name__ == "__main__":
	print flib(3)

