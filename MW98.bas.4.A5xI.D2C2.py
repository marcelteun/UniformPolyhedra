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

a0 = 1
a1 = 3
a2 = 2*tau
a3 = 2*tau - 1
a4 = tau
a5 = 2 * _tau
a6 = tau2
a7 = a6
a8 = 2
a9 = a3

t = tau * u
d = _tau * u
p = _tau2 * u
s = tau2 * u

a0 = a0 * u
a1 = a1 * u
a2 = a2 * u
a3 = a3 * u
a4 = a4 * u
a5 = a5 * u
a6 = a6 * u
a7 = a7 * u
a8 = a8 * u
a9 = a9 * u

Vs = [
	GeomTypes.Vec3([ a0,  u, a1]),
	GeomTypes.Vec3([-a0,  u, a1]),
	GeomTypes.Vec3([-a0, -u, a1]),
	GeomTypes.Vec3([ a0, -u, a1]),
]

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3],
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D2C2 O2 = [0, 0, 1]"
print "where D2C2 H2 _|_ O2 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
