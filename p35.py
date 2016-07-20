def ispr(n):
	d=2
	while d*d <= n:
		if n%d==0: return False
		d+=1
	return True

def rot(n):
	s=str(n)
	return [int(s[i:] + s[:i]) for i in range(len(s))]

print sum(all(ispr(e) for e in rot(n)) for n in range(2,1000000))
