jw=[-1]*1000
jw[0]=0
jw[1]=1
jw[89]=89
def c(n):
	if n<1000 and jw[n]!=-1: return jw[n]
	res = c(sum(int(c)**2 for c in str(n)))
	if n<1000: jw[n]=res
	return res
print sum(c(n)==89 for n in range(10000000))
