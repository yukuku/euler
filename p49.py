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

ps = set(genpr(10000))

print [(a,a+b,a+b+b) for a in range(1000, 10000) for b in range(1, (10000-a)/2) if a in ps and a+b in ps and a+b+b in ps and set(str(a))==set(str(a+b))==set(str(a+b+b))]
