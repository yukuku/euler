import math

def div(n):
	res = 0
	m = int(math.sqrt(n))
	if m*m == n:
		res = 1
		m2 = m-1
	else: m2 = m
	for d in range(1, m2+1):
		if n%d==0: res += 2
	return res

jum=0
for a in range(1, 100000):
	jum += a
	if div(jum) > 500:
		print jum
		break

