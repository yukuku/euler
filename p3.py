import math

def pf(n):
	res = []
	while True:
		found = False
		for p in range(2, int(math.sqrt(n))+1):
			if n%p == 0:
				n /= p
				res.append(p)
				found = True
				break
		if not found: break
	if n != 1: res.append(n)
	return res

print pf(600851475143)
