pp=set(n*(3*n-1)/2 for n in range(1, 1000001))
pm=max(pp)
hh=set(n*(2*n-1) for n in range(1, 1000001))
hm=max(hh)
for n in range(286, 1000001):
	t = n*(n+1)/2
	if t>pm or t>hm: raise ValueError()
	if t in pp and t in hh:
		print t
