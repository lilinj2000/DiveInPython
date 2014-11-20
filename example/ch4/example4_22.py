#! /usr/bin/python
import sys
sys.path.append('../../')

import odbchelper

object = odbchelper
method = "buildConnectionString"

print getattr(object, method)

print getattr(object, method).__doc__    
