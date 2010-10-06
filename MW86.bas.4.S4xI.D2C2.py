#!/usr/bin/python
import Geom3D
import math

u = 1
a = math.sqrt(2)/2
b = a + u

Vs = [
	[ a, b, a],
	[ a, a, b],
	[-a, a, b],
	[-a, b, a],
]

Fs = [
        [0, 1, 2, 3],
]

print "Use S4xI | D2C2"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D2C2 O2 = [0, 1, 1]"
print "where D2C2 H _|_ O2 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
