#!/usr/bin/python

import sys, os, re, unittest

def regressionTest():
    """"""
    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)
    print files

if __name__=='__main__':
    regressionTest()

    
