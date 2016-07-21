def ispr(n):
	if n==1: return False
	d=2
	while d*d<=n:
		if n%d==0: return False
		d+=1
	return True

def tr(n):
	return ispr(n) and all(ispr(int(str(n)[i:])) for i in range(1,len(str(n)))) and all(ispr(int(str(n)[:i])) for i in range(1,len(str(n))))

n=10
pp=[]
while True:
	for a in [n+1,n+3,n+7,n+9]:
		if tr(a):
			pp.append(a)
	if len(pp)==11: break
	n+=10
print sum(pp)
