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
	[ u, -a,  u],
	[ u,  u, -a],
	[-u,  u, -a],
	[-u, -a,  u],
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
