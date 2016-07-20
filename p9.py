def p(a,b,s):
	c=s-a-b
	return a*a+b*b==c*c
t=1000
print [(a,b,t-a-b,a*b*(t-a-b)) for a in range(1,t) for b in range(a,t) if a+b<t and p(a,b,t)]
