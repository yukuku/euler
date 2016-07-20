import math

def div(n):
	res = []
	m = int(math.sqrt(n))
	if m*m == n:
		res.append(m)
		m2 = m-1
	else: m2 = m
	for d in range(1, m2+1):
		if n%d==0:
			res.append(d)
			if d!=1: res.append(n/d)
	return res

def abu(n): return sum(div(n))>n

abus = set(n for n in range(28124) if abu(n))

def bisa(n):
	return any(n-x in abus for x in abus if x<n)

print sum(n for n in range(1, 28124) if not bisa(n))
