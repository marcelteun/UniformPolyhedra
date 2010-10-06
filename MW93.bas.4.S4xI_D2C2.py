#!/usr/bin/python

import math
import Geom3D

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
a = (V2 - 1) * u
b = (2*V2 - 1) * u

Vs = [
	[ b,  u, a],
	[ b, -u, a],
	[ a, -u, b],
	[ a,  u, b],
]

i = 0
for v in Vs:
    print "v_%02d" % i,
    i += 1
    for c in v:
	print "\t%0.16f" % c,
    print

Fs = [
        [0, 1, 2, 3],
]

i = 0
for f in Fs:
    print "f_%d" % i,
    i += 1
    for c in f:
	print "  %2d" % c,
    print

print "Use S4xI | D2C2"
print "where D2C2 O2 = [1, 0, 1]"
print "where D2C2 H _|_ O2 = [0, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs, Es = [0, 1, 1, 2, 2, 3, 3, 0])
