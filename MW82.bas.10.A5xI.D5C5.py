#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1
tau = (1 + math.sqrt(5))/2
tau2 = tau + 1
_tau = tau - 1
_tau2 = 2 - tau

v = 2 * u
t = tau * u
T = tau * v
q = tau2 * u
d = _tau * u
w = t + d

Vs = [
	GeomTypes.Vec3([ u, -d,  T]),
	GeomTypes.Vec3([ q,  0,  w]),
	GeomTypes.Vec3([ T,  u,  d]),
	GeomTypes.Vec3([ q,  v, -u]),
	GeomTypes.Vec3([ u,  q, -v]),
	GeomTypes.Vec3([-u,  q, -v]),
	GeomTypes.Vec3([-q,  v, -u]),
	GeomTypes.Vec3([-T,  u,  d]),
	GeomTypes.Vec3([-q,  0,  w]),
	GeomTypes.Vec3([-u, -d,  T]),
]

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5C5 O5 =", C_scaled
print "where D5C5 H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
