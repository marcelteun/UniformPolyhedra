#!/usr/bin/python

import math
import Geom3D

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
a = (V2 - 1) * u
b = (2*V2 - 1) * u

Vs = [
	[ b,  u,  a],
	[ a,  u,  b],

	[-u, -a,  b],
	[-u, -b,  a],

	[ a, -b, -u],
	[ b, -a, -u],
]

i = 0
for v in Vs:
    print "v_%02d" % i,
    i += 1
    for c in v:
	print "\t%0.16f" % c,
    print

Fs = [
        [0, 1, 2, 3, 4, 5],
]

Es = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 0]

i = 0
for f in Fs:
    print "f_%d" % i,
    i += 1
    for c in f:
	print "  %2d" % c,
    print

print "Use S4xI | D3C3"
print "where D3C3 O3 = [1, -1, 1]"
print "where D3C3 H _|_ O3 = [1, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs, Es = Es)
