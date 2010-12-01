#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2

A = [ 0,	1,	tau]

scale = tau
for i in range(len(A)):
	A[i] = A[i] / scale

Vs = [
	# 8 5 11
	GeomTypes.Vec3([-A[2],	 A[1],	 A[0]]),
	GeomTypes.Vec3([ A[0],	-A[2],	 A[1]]),
	GeomTypes.Vec3([ A[2],	 A[1],	 A[0]]),
]

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

Fs = [
        [0, 1, 2],
]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", [0, tau, 1]
print "----------------------------"
print "where D3C3 O3 = ", [0, 1/tau, tau]
print "where D3C3 H2 _|_ O3 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
