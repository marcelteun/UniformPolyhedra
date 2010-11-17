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

t = tau * u
s = tau2 * u
T = tau3 * u
d = _tau * u
w = _tau2 * u
D = _tau3 * u
r = tau + _tau

Vs = [
	GeomTypes.Vec3([ u,	-u,	r]),
	GeomTypes.Vec3([ 2*u,	d, 	t]),
	GeomTypes.Vec3([ u,	r,	u]),
	GeomTypes.Vec3([-u,	r,	u]),
	GeomTypes.Vec3([-2*u,	d, 	t]),
	GeomTypes.Vec3([-u,	-u,	r]),
]

Fs = [
        [0, 1, 2, 3, 4, 5],
]

O5 = [0, t, 1]

print "Use A5xI | D3C3"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", O5
print "----------------------------"
print "where D3C3 O3 = ", [0, d, t]
print "where D3C3 H2 _|_ O3 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
