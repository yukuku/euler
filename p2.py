def fib():
	a=1
	b=2
	while True:
		if a >= 4000000:
			raise StopIteration
		yield a
		a,b = b,a+b

print sum(i for i in fib() if i%2==0)
