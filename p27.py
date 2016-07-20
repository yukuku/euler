import math

def prsampe(sampe):
	pr=[2, 3]
	coba = 3
	while True:
		coba += 2
		yes = True
		m = math.sqrt(coba)
		for d in pr:
			if coba%d==0:
				yes = False
				break
			if d > m:
				break
		if yes:
			pr.append(coba)
				
		if coba > sampe:
			break
	return pr

pr = set(prsampe(2000000))

def prto(a,b):
	n = -1
	while True:
		c = n+1
		p = c*c + a*c + b
		if p > 2000000:
			raise ValueError()
		if p not in pr:
			return n
		n = c

print max(((a,b,a*b) for a in range(-999, 1000) for b in range(-999, 1000)), key=lambda e: prto(e[0], e[1]))
