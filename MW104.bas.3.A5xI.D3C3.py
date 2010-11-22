#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1
tau = (1 + math.sqrt(5))/2
tau2 = tau + 1
_tau = tau - 1

t = tau * u
T = tau * u * 2
q = tau2 * u
d = _tau * u
w = t + d

Vs = [
	GeomTypes.Vec3([ 0,  -w, q]),
	GeomTypes.Vec3([ q,  2*u, u]),
	GeomTypes.Vec3([-q,  2*u, u]),
]

Fs = [
        [0, 1, 2],
]

#l = len(Vs)
#for i in range(l):
#    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

O5 = [0, t, 1]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", O5
print "----------------------------"
print "where D3C3 O3 = ", [0, d, t]
print "where D3C3 H2 _|_ O3 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
