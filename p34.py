fc=[1,1,2,6,24,120,720,5040,40320,362880]

def ok(n):
	return n == sum(fc[ord(c)-48] for c in str(n))

print sum(x for x in range(10, 2540160+1) if ok(x))
