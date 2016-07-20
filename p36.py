def ok(n):
	b = bin(n)[2:]
	d = str(n)
	return d==d[::-1] and b==b[::-1]
print sum(n for n in range(1000000) if ok(n))
