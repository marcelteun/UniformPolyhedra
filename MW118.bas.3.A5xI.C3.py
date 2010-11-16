#!/usr/bin/python
import Geom3D
import GeomTypes
import math

f = 1
tau = (1 + math.sqrt(5))/2
_tau = tau - 1
_tau2 = 2 - tau
_tau3 = _tau * _tau2
tau2 = tau + 1
dtau = 2*tau
tau3 = dtau + 1

V = math.sqrt(3 * tau - 2)
W = tau * V

D = (3 - W)    * f
w = (_tau + V) * f
j = (W - 1 - 2 * _tau) * f
r = (V - _tau) * f
u = 2 * f
q = (tau2 - V) * f
S = (W - 1) * f
v = 2 * _tau * f


Vs = [
	GeomTypes.Vec3([ w,	0,	D]),
	GeomTypes.Vec3([-r,	u,	-j]),
	GeomTypes.Vec3([-v,	-S,	q]),
]

Fs = [
        [0, 1, 2],
]

O5 = [0, tau, 1]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", O5
print "----------------------------"
print "where C3 O3 = ", [0, _tau, tau]

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
