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

Pentagon = [
	# 36 48 30 42 54
	GeomTypes.Vec3([-A[10],	 A[9],	-A[11]]),
	GeomTypes.Vec3([-A[4],	 A[3],	-A[5]]),
	GeomTypes.Vec3([-A[13],	 A[12],	-A[14]]),
	GeomTypes.Vec3([-A[7],	 A[6],	-A[8]]),
	GeomTypes.Vec3([-A[1],	 A[0],	-A[2]]),
]

l = len(Pentagon)
#for i in range(l):
#    print "edge_ length:", (Pentagon[i] - Pentagon[(i+1)%l]).norm()

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
