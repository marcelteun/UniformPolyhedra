#!/usr/bin/python

import math
import Geom3D

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
a = (V2 - 1) * u
b = (2*V2 - 1) * u
d = u - a

Vs = [
	[ b,  d,  0],
	[ b,  u,  a],
	[ b,  a,  a],
	[ b,  a,  u],
	[ b,  0,  d],
	[ b, -a,  u],
	[ b, -a,  a],
	[ b, -u,  a],
	[ b, -d,  0],
	[ b, -u, -a],
	[ b, -a, -a],
	[ b, -a, -u],
	[ b,  0, -d],
	[ b,  a, -u],
	[ b,  a, -a],
	[ b,  u, -a],
]

i = 0
for v in Vs:
    print "v_%02d" % i,
    i += 1
    for c in v:
	print "\t%0.16f" % c,
    print

Fs = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        #[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

i = 0
for f in Fs:
    print "f_%d" % i,
    i += 1
    for c in f:
	print "  %2d" % c,
    print

print "Use S4xI | D4C4"
print "where D4C4 O4 = [1, 0, 0]"
print "where D4C4 H _|_ O4 = [0, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
