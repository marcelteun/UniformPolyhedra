#!/usr/bin/python
import Geom3D
import GeomTypes
import math

u = 1
tau = (1 + math.sqrt(5))/2
tau2 = tau + 1
dtau = 2*tau
tau3 = dtau + 1

t = tau * u
s = tau2 * u
T = tau3 * u

Vs = [
	GeomTypes.Vec3([ 0,  s, -2*u-t]),
	GeomTypes.Vec3([-T,  u,     -u]),
	GeomTypes.Vec3([-s, -t,   +2*t]),
	GeomTypes.Vec3([ s, -t,   +2*t]),
	GeomTypes.Vec3([ T,  u,     -u]),
]

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3, 4],
]

C_scaled = [0, t, 1] # scaled by 5/(tau2 + 1)

print "Use A5xI | D5C5"
print "where A5xI O3 = [1, 1, 1]"
print "where A5xI O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where D5C5 O5 =", C_scaled
print "where D5C5 H2 _|_ O5 = [1, 0, 0]"

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
