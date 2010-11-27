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
a = 0.79644210330606457
b = (a*a/tau + tau) / (a*tau - _tau)

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

Pentagon = [
	# 4 10 16 22 28
	GeomTypes.Vec3([-A[1],	A[2],	A[0]]),
	GeomTypes.Vec3([-A[4],	A[5],	A[3]]),
	GeomTypes.Vec3([-A[7],	A[8],	A[6]]),
	GeomTypes.Vec3([-A[10],	A[11],	A[9]]),
	GeomTypes.Vec3([-A[13],	A[14],	A[12]]),
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

print "Use A5 | C5"
print "where A5 O3 = [1, 1, 1]"
print "where A5 O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where C5 O5 =", C_scaled

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
