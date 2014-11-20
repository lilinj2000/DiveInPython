#! /usr/bin/python
import sys
sys.path.append('../../')

li = ["Larry", "Curly"]

print li.pop

print getattr(li, "pop")

print li

print getattr({}, "clear")

print getattr((), "clear")
