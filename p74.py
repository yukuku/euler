import math
f=[math.factorial(n) for n in range(10)]
def nx(n): return sum(f[ord(c)-48] for c in str(n))
spc={}
def le(n):
	ls=[n]
	while True:
		n=nx(n)
		if n in ls:
			if ls[0]==n: spc[n]=len(ls)
			return len(ls)
		if n in spc:
			res=len(ls)+spc[n]
			spc[ls[0]]=res
			return res
		ls.append(n)
print sum(le(n)==60 for n in range(1000000))
