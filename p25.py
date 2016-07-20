a=1
b=1
n=2
lim=pow(10,999)
while True:
	a,b=b,a+b
	n+=1
	if b>=lim:
		print n,b,len(str(b))
		break