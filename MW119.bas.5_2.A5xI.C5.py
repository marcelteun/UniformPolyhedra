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

Vtau = math.sqrt(tau)
_Vtau = 1.0 / Vtau
_Vtau3 = _Vtau * _Vtau * _Vtau

w = 2 * _tau
a0 = 2 * _Vtau
a1 = 1 - _Vtau3
a2 = _Vtau - _tau2
a3 = _tau + Vtau
a4 = _tau2 + _Vtau
a5 = a2 * tau
a6 = 1 + _Vtau3

Pentagon = [
	GeomTypes.Vec3([ a1,	a2,	a3]),
	GeomTypes.Vec3([ a6,	a4,	a5]),
	GeomTypes.Vec3([ a2,	a3,	-a1]),
	GeomTypes.Vec3([-w,	a0,	0]),
	GeomTypes.Vec3([-a4,	a5,	a6]),
]

l = len(Pentagon)

pentagon = []
for i in range(l):
    diagonal = Geom3D.Line3D(Pentagon[i], Pentagon[(i+2)%l])
    pentagon.append(diagonal.getPoint(_tau2))
    print "edge length:", (Pentagon[i] - Pentagon[(i+2)%l]).norm()

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

print "Use A5xI | C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where C5 O5 =", C_scaled

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
