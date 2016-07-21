def perm():
	s=[0]*10
	cc=[d for d in range(10)]
	res=[]
	m=[False]*10
	def p(i):
		if i==10:
			res.append(s[:])
		else:
			for idx in range(10):
				if not m[idx]:
					s[i]=cc[idx]
					m[idx]=True
					p(i+1)
					m[idx]=False
	p(0)
	return res

def cvt(s):
	return int(''.join(chr(48+c) for c in s))

print sum(cvt(s) for s in perm() if s[0] != 0 if cvt(s[1:4])%2==0 and cvt(s[2:5])%3==0 and cvt(s[3:6])%5==0 and cvt(s[4:7])%7==0 and cvt(s[5:8])%11==0 and cvt(s[6:9])%13==0 and cvt(s[7:10])%17==0)
