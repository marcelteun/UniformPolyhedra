#!/usr/bin/python
import Geom3D
import math

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
h = (V2 + 1) * u
a = (V2 - 1) * u

e = a * V2

Vs = [
	[-a,  u,  h],
	[ u, -a,  h],
	[ h, -a,  u],
	[ h,  u, -a],
	[ u,  h, -a],
	[-a,  h,  u],
]

Fs = [
        [0, 1, 2, 3, 4, 5],
]

print "Use S4xI | D3C3"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D3C3 O3 = [1, 1, 1]"
print "where D3C3 H _|_ O2 = [1, -1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
