#!/usr/bin/python
import Geom3D
import math

u = 1
a = math.sqrt(2)/2
b = a + u

Vs = [
	[ u,  0, u],
	[ 0,  u, u],
	[-u,  0, u],
	[ 0, -u, u],
]

Fs = [
        [0, 1, 2, 3],
]

print "Use S4xI | D4C4"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D4C4 O4 = [0, 0, 1]"
print "where D4C4 H _|_ O4 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
