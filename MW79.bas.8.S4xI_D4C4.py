#!/usr/bin/python

import math
import Geom3D

V = lambda x: math.sqrt(x)
V2 = V(2)

u = 1
h = (V2 + 1) * u
a = (V2 - 1) * u

Vs = [
        [ u,  h, a],
        [-u,  h, a],
        [-h,  u, a],
        [-h, -u, a],
        [-u, -h, a],
        [ u, -h, a],
        [ h, -u, a],
        [ h,  u, a],
]

Fs = [
        [0, 1, 2, 3, 4, 5, 6, 7],
]

print "Use S4xI | D4C4"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D4C4 O4 = [0, 0, 1]"
print "where D4C4 H _|_ O4 = [0, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
