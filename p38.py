def p(k):
	s = str(k)
	if '0' in s: return False
	n=2
	while True:
		s += str(k*n)
		if '0' not in s and len(s)==9 and len(set(s))==9:
			print k,s
			return True
		if len(s)>9: return False
		n+=1

for k in range(10000): p(k)
