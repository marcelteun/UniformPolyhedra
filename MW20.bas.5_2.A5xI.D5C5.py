#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2
_tau2 = 2 - tau

A = [ 0,	1,	tau]

scale = tau
for i in range(len(A)):
	A[i] = A[i] / scale

Pentagon = [
	# 0 1 11 6 8
	GeomTypes.Vec3([-A[1],	 A[0],	 A[2]]),
	GeomTypes.Vec3([ A[1],	 A[0],	 A[2]]),
	GeomTypes.Vec3([ A[2],	 A[1],	 A[0]]),
	GeomTypes.Vec3([ A[0],	 A[2],	-A[1]]),
	GeomTypes.Vec3([-A[2],	 A[1],	 A[0]]),
]

l = len(Pentagon)

pentagon = []
for i in range(l):
    diagonal = Geom3D.Line3D(Pentagon[i], Pentagon[(i+2)%l])
    pentagon.append(diagonal.getPoint(_tau2))
    print "edge length: %0.15f" % (Pentagon[i] - Pentagon[(i+2)%l]).norm()

Vs = []
for i in range(l):
    Vs.append(Pentagon[i])
    Vs.append(pentagon[i])

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

C_scaled = [0, tau, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5C5 O5 =", C_scaled
print "where D5C5 H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
