from numpy import poly1d
from numpy import sqrt


tau = (sqrt(5) + 1) / 2
tau2 = tau + 1
mw111 =  poly1d([tau, -1, 2, -1, 1 - tau])
print mw111
print '---> roots:', mw111.r

a = mw111.r[2].real
print '***** MW 111 ********'
print 'a = %.32f' % a
print 'B = %.32f' % ((a*a/tau + tau) / (a*tau - 1.0/tau))
print '^^^^^^^^^^^^^^^^^^^^^'

mw112 =  poly1d([1, 0, -1, -1])
print '---> roots:', mw112.r
rho = mw112.r[0].real
rho2 = rho*rho
print mw112
print '***** MW 112 ********'
print 'rho = %.32f' % rho
print 'a   = %.32f' % (rho + 1)
print 'B   = %.32f' % (tau2*rho2 + tau2*rho + tau)
print 'y   = %.32f' % (rho2 + tau*rho)
print '^^^^^^^^^^^^^^^^^^^^^'

mw113 =  poly1d([1, 0, -2, tau - 1])
print '---> roots:', mw113.r
xi = mw113.r[0].real
a = xi - 1.0/xi
b = -xi/tau + 1.0/tau2 - 1.0/(xi*tau)
print '***** MW 113 ********'
print 'xi = %.32f' % xi
print 'a   = %.32f' % a
print 'B   = %.32f' % b
print '^^^^^^^^^^^^^^^^^^^^^'

xi = mw113.r[1].real
a = xi - 1.0/xi
b = -xi/tau + 1.0/tau2 - 1.0/(xi*tau)
print '***** MW 116 ********'
print 'xi = %.32f' % xi
print 'a   = %.32f' % a
print 'B   = %.32f' % b
print '^^^^^^^^^^^^^^^^^^^^^'
