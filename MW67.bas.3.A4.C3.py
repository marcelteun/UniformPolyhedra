#!/usr/bin/python
import Geom3D

u = 1

Vs = [
	[ u, 0, 0],
	[ 0, u, 0],
	[ 0, 0, u],
]

Fs = [
        [0, 1, 2],
]

print "Use A4 | C3"
print "where A4 H0 = [1, 0, 0]"
print "where A4 H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where C3 O2 = [1, 1, 1]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
