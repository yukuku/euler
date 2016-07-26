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

pp=genpr(1000000)
ps=set(pp)

mx=999999

mxn=0
mxz=0
for a in range(len(pp)):
	zum=pp[a]
	n=1
	if zum > mx: break
	for b in range(a+1, len(pp)):
		zum+=pp[b]
		n+=1
		if zum > mx: break
		if zum in ps and n>mxn:
			mxn=n
			mxz=zum
			print pp[a], n, zum
