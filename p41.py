def ispr(n):
	if n==1: return False
	if n%2==0: return False
	d=3
	while d*d<=n:
		if n%d==0: return False
		d+=2
	return True

def p(n):
	if n%5==0: return False
	s=str(n)
	if '0' in s: return False
	if any(chr(48+i) in s for i in range(len(s)+1,10)): return False
	if len(set(c for c in s))!=len(s): return False
	res = ispr(n)
	if res:
		print n
	return res

print [n for n in range(3,10000000,2) if p(n)]
