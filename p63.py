import math

def c(n):
	mi=10**(n-1)
	bi=mi**(1.0/n)
	res = int(9-math.ceil(bi)+1)
	print n,bi,res
	return res

print sum(c(n) for n in range(1,26))