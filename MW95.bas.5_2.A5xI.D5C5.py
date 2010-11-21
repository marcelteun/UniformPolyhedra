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

d = _tau * u
D = (1 + _tau2) * u
pd = _tau3 * u

Pentagon = [
	GeomTypes.Vec3([ 0,	u,	3*d]),
	GeomTypes.Vec3([ u,	D,	2*d]),
	GeomTypes.Vec3([ d,	2*u,	pd]),
	GeomTypes.Vec3([-d,	2*u,	pd]),
	GeomTypes.Vec3([-u,	D,	2*d]),
]

l = len(Pentagon)

pentagon = []
for i in range(l):
    diagonal = Geom3D.Line3D(Pentagon[i], Pentagon[(i+2)%l])
    pentagon.append(diagonal.getPoint(_tau2))
    #print "edge length:", (Pentagon[i] - Pentagon[(i+2)%l]).norm()

Vs = []
for i in range(l):
    Vs.append(Pentagon[i])
    Vs.append(pentagon[i])

#for v in Vs:
#    print v

Fs = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
]

C_scaled = [0, tau, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5C5 O5 =", C_scaled
print "where D5C5 H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
