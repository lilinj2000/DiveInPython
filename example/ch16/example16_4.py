#!/usr/bin/python

import os

print os.getcwd()

print os.path.abspath('')

print os.path.abspath('.ssh')

print os.path.abspath('/home/you/.ssh')

print os.path.abspath('.ssh/../foo/')
