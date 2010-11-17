#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1
tau = (1 + math.sqrt(5))/2
_tau = tau - 1
_tau2 = 2 - tau
_tau3 = _tau * _tau2
tau2 = tau + 1
dtau = 2*tau
tau3 = dtau + 1

V0 = math.sqrt(3 * tau - 2)

t = (1 + tau * V0) * u / 2
s = (3 + tau * V0) * u / 2
T = (tau2 + V0) * u / 2
d = _tau * u
w = (V0 - _tau) * u / 2
v = (_tau + V0) * u / 2
r = (1 + 2 * _tau + tau * V0) * u / 2

Vs = [
	GeomTypes.Vec3([-w,	0,	s]),
	GeomTypes.Vec3([ v,	u,	r]),
	GeomTypes.Vec3([-d,	t, 	T]),
]

Fs = [
        [0, 1, 2],
]

#l = len(Vs)
#for i in range(l):
#    print "edge length:", (Vs[i] - Vs[(i+2)%l]).norm()

O5 = [0, tau, 1]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", O5
print "----------------------------"
print "where C3 O3 = ", [0, _tau, tau]

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
