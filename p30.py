def ok(n):
	return n == sum((ord(c)-48)**5 for c in str(n))

print sum(x for x in range(10, 354295) if ok(x))

