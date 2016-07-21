import math

def p(a,b,n):
	s=str(a)+str(b)+str(n)
	return len(s)==9 and '0' not in s and len(set(c for c in s))==9

def t(n):
	for a in range(1, int(math.ceil(math.sqrt(n)))):
		if n%a==0:
			b = n/a
			if p(a,b,n):
				print a,b,n
				return True
	return False

print sum(n for n in range(1000, 100000) if t(n))
