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

def ami(n):
	b=sum(div(n))
	return sum(div(b))==n

print sum(n for n in range(10000) if ami(n))
