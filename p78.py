import sys
sys.setrecursionlimit(10000)

jw={}

def c(n,m):
	if n==0 or n==1 or m==1: return 1
	if m>n: return c(n,n)
	if (n,m) in jw: return jw[(n,m)]
	res=c(n-m,m)+c(n,m-1)
	res%=1000000
	jw[(n,m)]=res
	return res

import itertools
for n in itertools.count(1):
	print n
	if c(n,n)%1000000==0:
		print 'xxxxxx', n
		break
