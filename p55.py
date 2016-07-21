def pal(n):
	s=str(n)
	return s==s[::-1]

def isl(n):
	for it in range(50):
		n=n+int(str(n)[::-1])
		if pal(n): return False
	return True

print sum(isl(n) for n in range(10000))
