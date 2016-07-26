def inv(n): return (n[1],n[0])
def plus1(n): return (n[0]+n[1],n[1])
def plus2(n): return (n[0]+2*n[1],n[1])

n=(1,2)
res=0
for a in range(1000):
	cek=plus1(n)
	print cek
	if len(str(cek[0]))>len(str(cek[1])): res += 1
	n=plus2(n)
	n=inv(n)

print res
