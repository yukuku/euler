def ispr(n):
	if n==1: return False
	if n==2: return True
	d=3
	while d*d<=n:
		if n%d==0: return False
		d+=2
	return True

def k(n): return 3+n*10+n*(n-1)*8/2


p=0
np=1
for n in range(20000):
	b=k(n)
	x=(ispr(b), ispr(b+2*(n+1)), ispr(b+4*(n+1)), ispr(b+6*(n+1)))
	p+=sum(x)
	np+=sum(1-c for c in x)
	if 1.0*p/(p+np) < 0.1:
		print p, np, 2*(n+1)+1
		break
