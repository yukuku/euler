s=[chr(48+a) for a in range(10)]
def fak(n): return reduce(lambda a,b:a*b,range(1,n+1),1)
def p(pre, s, n):
	cp=fak(len(s)-1)
	i=n/cp
	pre+=s[i]
	cs=s[:]
	cs.remove(s[i])
	if len(cs)==0:
		return pre
	return p(pre, cs, n%cp)

print p('', s, 1000000-1)

