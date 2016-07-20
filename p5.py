def gcd(a,b):
	if b>a: a,b=b,a
	while True:
		if b==0: return a
		a %= b
		a,b=b,a

def kpk(a,b):
	return a*b/gcd(a,b)

res = 1
for i in range(1, 21):
	res = kpk(res, i)
print res

# alasan:
# max(a,b) = a+b-min(a,b)
# 2   1 4  5 1  4
# 3   1    1
# 5   2    2
# 11    1  1
