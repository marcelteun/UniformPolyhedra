#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2
_tau = tau - 1
tau2 = tau + 1
_tau2 = 2 - tau

# calculated with numpy from polynom with coefs: [tau, -1, +2, -1, 1 - tau]
# source: wikipedia.org
a = -0.33520896790783666352453451509064
b = (a*a/tau + tau) / (a*tau - _tau)

A = [
     2*a,		 2,			2*b,
     a + b/tau + tau, 	-a*tau + b + _tau, 	a/tau + b*tau - 1,
    -a/tau + b*tau + 1, -a + b/tau - tau, 	a*tau + b - _tau,
    -a/tau + b*tau - 1,  a - b/tau - tau, 	a*tau + b + _tau,
     a + b/tau - tau, 	 a*tau - b + _tau, 	a/tau + b*tau + 1,
]

scale = 4.21874872855/2
for i in range(len(A)):
	A[i] = A[i] / scale

Vs = [
	# 49 47 59
	GeomTypes.Vec3([-A[3],	-A[4],	-A[5]]),
	GeomTypes.Vec3([-A[7],	-A[8],	-A[6]]),
	GeomTypes.Vec3([-A[1],	-A[2],	-A[0]]),
]

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

Fs = [
        [0, 1, 2],
]

O5 = [0, tau, 1]

print "Use A5 | C3"
print "where A5 O3 = [1, 1, 1]"
print "where A5 O5 _|_ O3 =", O5

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
