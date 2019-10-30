from __future__ import unicode_literals
import datetime as dt
import numpy as np
n = 100000
start = dt.datetime.now()
A,B = [],[]
for i in range(n):
	A.append(i**2)
	B.append(i**3)
C=[]
for a,b in zip(A,B):
	C.append(a+b)
print((dt.datetime.now()-start).microseconds)
start = dt.datetime.now()
A,B = np.arange(n)**2,np.arange(n)**3
C=A+B
print((dt.datetime.now()-start).microseconds)

e = np.array([0x1234],dtype=('u2',{'lo':('u1',0),'hi':('u1',1)}))
print('{:x} {:x} {:x}'.format(e[0],e['lo'][0],e['hi'][0]))