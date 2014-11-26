#! /usr/bin/python

def fibonacci(max):
    """"""
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

if __name__=='__main__':
    for n in fibonacci(1000):
        print n,



    

