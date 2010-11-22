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

a0 = _tau
a1 = 3
a2 = 2*tau
a3 = 2
a4 = tau
a5 = tau
a6 = 3 - _tau
a7 = 3*_tau + 1
a8 = tau
a9 = 2*_tau + 1
a10 = 2*_tau
a11 = 2*_tau - 1
a12 = _tau
a13 = 2 - _tau

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

Decagon = [
	GeomTypes.Vec3([ a0,	 a10,	 a1]),
	GeomTypes.Vec3([ a4,	 a5,	 a6]),
	GeomTypes.Vec3([ a3,	 a9,	 a13]),
	GeomTypes.Vec3([ a8,	 a7,	 p]),
	GeomTypes.Vec3([ a12,	 a2,	-a11]),

	GeomTypes.Vec3([-a12,	 a2,	-a11]),
	GeomTypes.Vec3([-a8,	 a7,	 p]),
	GeomTypes.Vec3([-a3,	 a9,	 a13]),
	GeomTypes.Vec3([-a4,	 a5,	 a6]),
	GeomTypes.Vec3([-a0,	 a10,	 a1]),
]

decagon = []
_tau2 = 2*tau - 3
for i in range(l):
    diagonal = Geom3D.Line3D(Decagon[i], Decagon[(i+3)%l])
    decagon.append(diagonal.getPoint(_tau2))
    #print "edge length:", (Decagon[i] - Decagon[(i+3)%l]).norm()

Vs = []
for i in range(l):
    Vs.append(Decagon[i])
    Vs.append(decagon[i])

#for v in Vs:
#    print v

Fs = [
        [       0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19
        ]
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5xI O5 =", C_scaled
print "where D5xI H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
