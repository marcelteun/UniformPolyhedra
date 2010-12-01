#!/usr/bin/python
import Geom3D
import math

Vs = [
	[-1,  1,  1],
	[ 1, -1,  1],
	[ 1,  1, -1],
]

Fs = [
        [0, 1, 2],
]

print "Use S4xI | D3C3"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H1 = [0, 1, 0]"
print "----------------------------"
print "where D3C3 O3 = [1, 1, 1]"
print "where D3C3 H_|_ O3 = [1, -1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
