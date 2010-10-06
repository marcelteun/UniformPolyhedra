#!/usr/bin/python

import math
import Geom3D

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
a = (V2 - 1) * u
#b = (2*V2 - 1) * u
d = u - a

Vs = [
	[ a,  u,  a],
        [ a, -a, -u],
	[-u, -a,  a],
]

i = 0
for v in Vs:
    print "v_%02d" % i,
    i += 1
    for c in v:
	print "\t%0.16f" % c,
    print

Fs = [
        [0, 1, 2],
]

i = 0
for f in Fs:
    print "f_%d" % i,
    i += 1
    for c in f:
	print "  %2d" % c,
    print

print "Use S4xI | D3C3"
print "where D3C3 O3 = [-1, 1, -1]"
print "where D3C3 O3 _|_ = [-1, 0, 1]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
