#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1.0
tau = (1 + math.sqrt(5))/2
_tau = tau - 1
_tau2 = 2 - tau
_tau3 = _tau * _tau2
tau2 = tau + 1
dtau = 2*tau
tau3 = dtau + 1

V0 = math.sqrt(3 * tau - 2)

d = _tau * u
D = (1 + _tau2) * u
pd = _tau3 * u



Vs = [
        GeomTypes.Vec3([ u,	-D,	 2*d]),
        GeomTypes.Vec3([ 2*u,	 pd,	 d]),
        GeomTypes.Vec3([ u,	 3*d,	 0]),
        GeomTypes.Vec3([-u,	 3*d,	 0]),
        GeomTypes.Vec3([-2*u,	 pd,	 d]),
        GeomTypes.Vec3([-u,	-D,	 2*d]),
]

#l = len(Vs)
#for i in range(l):
#    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

Fs = [
        [0, 1, 2, 3, 4, 5],
]

O5 = [0, tau, 1]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", O5
print "----------------------------"
print "where D3C3 O3 = ", [0, _tau, tau]
print "where D3C3 H2 _|_ O3 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
