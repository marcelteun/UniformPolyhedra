#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2
_tau = tau - 1
tau2 = tau + 1
_tau2 = 2 - tau

# calculated with numpy from polynom with coefs: [1, 0, -2, tau - 1]
# source: wikipedia.org
xi = 1.22247266696100220784160228504334
a = xi - 1.0/xi
b = -xi/tau + _tau2 - 1.0/(xi*tau)

A = [
     2*a,		 2,			 2*b,
     a - b*tau - _tau,	 a/tau + b - tau, 	-a*tau - b/tau - 1,
     a*tau - b/tau + 1, -a - b*tau + _tau, 	-a/tau + b + tau,
     a*tau - b/tau - 1,  a + b*tau + _tau, 	-a/tau + b - tau,
     a - b*tau + _tau,	-a/tau - b - tau, 	-a*tau - b/tau + 1,
]

scale = 4.31478695085 / 2
for i in range(len(A)):
	A[i] = A[i] / scale

Vs = [
	# 4 14 10 ( not 8 neither 20: 2 edges 2 other: 2.44494533392)
	GeomTypes.Vec3([-A[2],	-A[1],	 A[0]]),
	GeomTypes.Vec3([-A[6],	-A[8],	 A[7]]),
	GeomTypes.Vec3([-A[5],	-A[4],	 A[3]]),
]

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

Fs = [
        [0, 2, 1],
]

O5 = [0, tau, 1]

print "Use A5 | E"
print "where A5 O3 = [1, 1, 1]"
print "where A5 O5 _|_ O3 =", O5

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
