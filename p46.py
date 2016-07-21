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

pp = genpr(1000000)
ss = set(2*n*n for n in range(1, 1000))

def t(n):
	for p in pp:
		if p >= n: return False
		if n-p in ss: return True

ps = set(pp)
for n in range(3, 1000000, 2):
	if n not in pp:
		if not t(n):
			print n
			break
