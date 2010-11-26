#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2
_tau = tau - 1
tau2 = tau + 1

chi = math.sqrt(tau - 5.0/27)
xi = math.pow((tau + chi)/2, 1.0 / 3) + math.pow((tau - chi)/2, 1.0 / 3)
a = xi - 1.0/xi
b = tau*xi + tau2 + tau/xi
A = [
     2*a,		 2,			2*b,
     a + b/tau + tau, 	-a*tau + b + _tau, 	a/tau + b*tau - 1,
    -a/tau + b*tau + 1, -a + b/tau - tau, 	a*tau + b - _tau,
    -a/tau + b*tau - 1,  a - b/tau - tau, 	a*tau + b + _tau,
     a + b/tau - tau, 	 a*tau - b + _tau, 	a/tau + b*tau + 1,
]

scale = 0.3
for i in range(len(A)):
	A[i] = scale * A[i]

Vs = [
	# 0 1 25
	GeomTypes.Vec3([-A[0],	 A[1],	A[2]]),
	GeomTypes.Vec3([ A[0],	-A[1],	A[2]]),
	GeomTypes.Vec3([ A[12],	-A[13],	A[14]]),
]

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

Fs = [
        [0, 1, 2],
]

O5 = [0, tau, 1]

print "Use A5 | E"
print "where A5 O3 = [1, 1, 1]"
print "where A5 O5 _|_ O3 =", O5

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
