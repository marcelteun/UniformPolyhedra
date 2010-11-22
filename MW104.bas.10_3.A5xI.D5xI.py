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

Decagon = [
	GeomTypes.Vec3([ u,	-d,	 2*t]),
	GeomTypes.Vec3([ q,	 0,	 w]),
	GeomTypes.Vec3([ 2*t,	 u,	 d]),
	GeomTypes.Vec3([ q,	 2*u,	-u]),
	GeomTypes.Vec3([ u,	 q,	-2*u]),

	GeomTypes.Vec3([-u,	 q,	-2*u]),
	GeomTypes.Vec3([-q,	 2*u,	-u]),
	GeomTypes.Vec3([-2*t,	 u,	 d]),
	GeomTypes.Vec3([-q,	 0,	 w]),
	GeomTypes.Vec3([-u,	-d,	 2*t]),
]

l = len(Decagon)

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
