def bc(n):
	s=str(n)
	t=s[0]
	up=False
	dn=False
	for c in s[1:]:
		if c>t: up=True
		elif c<t: dn=True
		if up and dn: return True
		t=c
	return False

b=0
nb=99

from itertools import count as cnt
for n in cnt(100):
	if bc(n): b+=1
	else: nb+=1
	if b==nb*99:
		print n,b,nb,float(b)/(b+nb)
		break
