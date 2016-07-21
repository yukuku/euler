import math

def sol(p):
	res=[]
	for a in range(1, int(math.ceil(p/2))):
		for b in range(1, min(a, int(math.ceil((p-a)/2)))):
			c=p-a-b
			if a*a+b*b==c*c:
				res.append((b,a,c))
	return res

print max((p for p in range(1001)), key=lambda e: len(sol(e)))
