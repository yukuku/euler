def a(n):
	return pow(sum(i for i in range(1,n+1)),2) - sum(i*i for i in range(1,n+1))
print a(100)
