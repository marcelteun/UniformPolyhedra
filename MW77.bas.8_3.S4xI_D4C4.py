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

e = a * V2

Vs = [
        [ u,  a, u],
        [ a,  a, u],
        [ a,  u, u],
        [ 0,  e, u],
        [-a,  u, u],
        [-a,  a, u],
        [-u,  a, u],
        [-e,  0, u],
        [-u, -a, u],
        [-a, -a, u],
        [-a, -u, u],
        [ 0, -e, u],
        [ a, -u, u],
        [ a, -a, u],
        [ u, -a, u],
        [ e,  0, u],
]

Fs = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
]

print "Use S4xI | D4C4"
print "where S4xI H0 = [1, 0, 0]"
print "where S4xI H1 _|_ H0 = [0, 1, 0]"
print "----------------------------"
print "where D4C4 O4 = [0, 0, 1]"
print "where D4C4 H _|_ O4 = [0, 1, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
