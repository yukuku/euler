jw={}

def c(n,m):
	print (n,m)
	if n==0 or n==1: return 1
	if (n,m) in jw: return jw[(n,m)]
	res=0
	for i in range(1,min(n+1,m+1)):
		res+=c(n-i,i)
	jw[(n,m)]=res
	return res

print c(100,100)-1