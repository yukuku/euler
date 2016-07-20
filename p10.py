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

print sum(prsampe(2000000))
