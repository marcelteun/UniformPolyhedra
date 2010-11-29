#!/usr/bin/python
import Geom3D
import GeomTypes
import math

tau = (1 + math.sqrt(5))/2
_tau = tau - 1
tau2 = tau + 1
_tau2 = 2 - tau

w = lambda x: math.pow(x, 1.0/3)

# calculated with numpy from polynom with coefs: [1, 0, -1, -1]
# source: wikipedia.org
rho = 1.32471795724474517008673046802869
rho2 = rho*rho
a = (rho + 1)
b = (tau2*rho2 + tau2*rho + tau)
c = (rho2 + tau*rho)

A = [
     2*a,		 2*c,			2*b,
     a + b/tau + c*tau,	-a*tau + b + c/tau, 	a/tau + b*tau - c,
    -a/tau + b*tau + c, -a + b/tau - c*tau, 	a*tau + b - c/tau,
    -a/tau + b*tau - c,  a - b/tau - c*tau, 	a*tau + b + c/tau,
     a + b/tau - c*tau,  a*tau - b + c/tau, 	a/tau + b*tau + c,
]

scale = 18.9755542467 / 2
for i in range(len(A)):
	A[i] = A[i] / scale

Vs = [
	# 6 25 38 58 14
	GeomTypes.Vec3([-A[3],	 A[4],	 A[5]]),
	GeomTypes.Vec3([ A[12],	-A[13],	 A[14]]),
	GeomTypes.Vec3([ A[11],	 A[9],	-A[10]]),
	GeomTypes.Vec3([ A[1],	 A[2],	-A[0]]),
	GeomTypes.Vec3([-A[8],	 A[6],	 A[7]]),
]
Vs = Vs

l = len(Vs)
for i in range(l):
    print "edge length:", (Vs[i] - Vs[(i+1)%l]).norm()

#for v in Vs:
#    print v

Fs = [
        [0, 1, 2, 3, 4],
]

C_scaled = [0, tau, 1] # scaled by 5/(tau2 + 1)

print "Use A5 | C5"
print "where A5 O3 = [1, 1, 1]"
print "where A5 O5 _|_ O3 =", C_scaled
print "----------------------------"
print "where C5 O5 =", C_scaled

shape = Geom3D.SimpleShape(Vs = Vs, Fs = Fs)
