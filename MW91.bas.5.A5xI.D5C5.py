#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1.0
tau = (1 + math.sqrt(5))/2
tau2 = tau + 1
_tau = tau - 1
_tau2 = 2 - tau

t = tau * u
d = _tau * u
s = tau2 * u

Vs = [
	GeomTypes.Vec3([ u,  t,  s])/2,
	GeomTypes.Vec3([ t,  s,  u])/2,
	GeomTypes.Vec3([ 0,  t,  0]),
	GeomTypes.Vec3([-t,  s,  u])/2,
	GeomTypes.Vec3([-u,  t,  s])/2,
]

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3, 4]
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5xI O5 =", C_scaled
print "where D5xI H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
