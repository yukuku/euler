def a(n):
	res = 1
	while True:
		if n == 1:
			break
		res+=1
		if n%2==0:
			n/=2
		else:
			n=3*n+1
	return res

print max(a(n) for n in range(1, 1000000))

