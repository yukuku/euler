def genpr(max):
	res=[2]
	for n in range(3, max, 2):
		p=True
		for d in res:
			if d*d>n:
				break
			if n%d==0:
				p=False
				break
		if p: res.append(n)
	return res

pp = genpr(100000)

def dpf(n): # does not work for primes
	res=0
	for p in pp:
		if 2*p>n:
			break
		if n%p==0: res+=1
	return res

a,b,c=0,0,0
n=2
while True:
	d=dpf(n+3)
	if d!=4:
		n=n+4
		a,b,c=0,0,0
		continue
	if 4==a==b==c==d:
		print n
		break
	a,b,c=b,c,d
	n+=1
