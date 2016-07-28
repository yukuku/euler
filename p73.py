import math

t=1.0/3
u=1.0/2

def gcd(a,b):
	if b>a: a,b=b,a
	while True:
		a,b=b%a,a
		if a==0: return b

res=0
for d in range(4,12001):
	if d%3==0: mi=d/3+1
	else: mi=int(t*d)+1
	if d%2==0: ma=d/2-1
	else: ma=int(u*d)
	for n in range(mi,ma+1):
		if gcd(n,d)==1: 
			res+=1

print res
