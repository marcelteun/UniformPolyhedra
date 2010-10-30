#!/usr/bin/python

import math
import Geom3D

V2 = math.sqrt(2)

u = 1
a = V2 - 1

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
a = (V2 - 1) * u
b = (2*V2 - 1) * u
d = u - a

Vs = [
	[ u,  u, a],
	[-u,  u, a],
	[-u, -u, a],
	[ u, -u, a],
]

Fs = [
        [0, 1, 2, 3],
]

print "Use S4xI | D4C4"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D4C4 O4 = [0, 0, 1]"
print "where D4C4 H _|_ O4 = [0, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
