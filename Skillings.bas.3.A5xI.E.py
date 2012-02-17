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

Vs = [
	GeomTypes.Vec3([-a4,	-a5,	 a6]),
	GeomTypes.Vec3([ a6,	-a4,	 a5]),
	GeomTypes.Vec3([ a5,	 a6,	 a4]),
]

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

#for v in Vs:
#    print v

Fs = [
        [1, 2, 0],
]

C_scaled = [0, tau, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | E"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
