import math

def prsampe(n):
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
				
		if len(pr) > n:
			break
	return pr[:n]

print prsampe(10001)
