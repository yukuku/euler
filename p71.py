t=3.0/7
mi=999
for d in range(1,1000001):
	if d%7==0: continue
	n=int(t*d)
	jr=t-float(n)/d
	if jr<mi:
		print jr,n,d
		mi=jr
