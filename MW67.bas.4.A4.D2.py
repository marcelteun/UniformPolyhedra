#!/usr/bin/python
import Geom3D

u = 1

Vs = [
	[ u,  0, 0],
	[ 0, -u, 0],
	[-u,  0, 0],
	[ 0,  u, 0],
]

Fs = [
        [0, 1, 2, 3],
]

print "Use A4 | D2"
print "where A4 H0 = [1, 0, 0]"
print "where A4 H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D2 O2 = [0, 0, 1]"
print "where D2 H _|_ O2 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
