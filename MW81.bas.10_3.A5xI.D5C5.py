#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1
tau = (1 + math.sqrt(5))/2
tau2 = tau + 1
tau3 = 2*tau + 1
_tau = tau - 1

t = tau * u
s = tau2 * u
T = tau3 * u
d = _tau * u

Decagon = [
	GeomTypes.Vec3([    -d,     t, 2*t]),
	GeomTypes.Vec3([    -t,   2*u,   s]),
	GeomTypes.Vec3([  -2*u,     s,   t]),
	GeomTypes.Vec3([    -t,   2*t,   d]),
	GeomTypes.Vec3([    -d, 2*u+t,   0]),
	GeomTypes.Vec3([     d, 2*u+t,   0]),
	GeomTypes.Vec3([     t,   2*t,   d]),
	GeomTypes.Vec3([   2*u,     s,   t]),
	GeomTypes.Vec3([     t,   2*u,   s]),
	GeomTypes.Vec3([     d,     t, 2*t]),
]

l = len(Decagon)

decagon = []
_tau2 = 2*tau - 3
for i in range(l):
    diagonal = Geom3D.Line3D(Decagon[i], Decagon[(i+3)%l])
    decagon.append(diagonal.getPoint(_tau2))

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
print "where D5C5 O5 =", C_scaled
print "where D5C5 H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
