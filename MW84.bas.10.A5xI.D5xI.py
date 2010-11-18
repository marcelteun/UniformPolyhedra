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

a0 = 2 - _tau
a1 = 2 + tau
a2 = 3*tau - 1
a3 = a2 - 1

t = tau * u
d = _tau * u
p = _tau2 * u
s = tau2 * u

a0 = a0 * u
a1 = a1 * u
a2 = a2 * u
a3 = a3 * u

a4 = 2 * u
a5 = 2 * d
a6 = 2 * t
a7 = 3 * u

Decagon = [

	GeomTypes.Vec3([-u,	 p,	 a2]),
	GeomTypes.Vec3([-s,	 u,	 a3]),
	GeomTypes.Vec3([-a6,	 a4,	 a5]),
	GeomTypes.Vec3([-s,	 a7,	-p]),
	GeomTypes.Vec3([-u,	 a1,	-a0]),
	GeomTypes.Vec3([ u,	 a1,	-a0]),
	GeomTypes.Vec3([ s,	 a7,	-p]),
	GeomTypes.Vec3([ a6,	 a4,	 a5]),
	GeomTypes.Vec3([ s,	 u,	 a3]),
	GeomTypes.Vec3([ u,	 p,	 a2]),

]

#l = len(Decagon)
#for i in range(l):
#    print "edge length:", (Decagon[i] - Decagon[(i+1)%l]).norm()

Fs = [
        [       0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        ]
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5xI O5 =", C_scaled
print "where D5xI H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Decagon, Fs = Fs)
