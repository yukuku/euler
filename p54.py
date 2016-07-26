ss=[line.split() for line in open('p054_poker.txt').readlines()]
m={'T':10,'J':11,'Q':12,'K':13,'A':14}
def v(c): return int(c[0]) if c[0] <= '9' else m[c[0]]
def u(c): return c[1]

def allsame(l):
	l=list(l)
	if len(l)==0: return True
	return all(x==l[0] for x in l)

def increasing(l):
	l=list(l)
	if len(l)==0: return True
	return all(x==l[0]+i for i,x in enumerate(l))

def _rf(s):
	if [v(c) for c in s] != [10,11,12,13,14]: return 0
	return int(allsame(u(c) for c in s))

def _sf(s):
	if not allsame(u(c) for c in s): return 0
	if not increasing(v(c) for c in s): return 0
	return v(s[4])

def _fk(s):
	if allsame(v(c) for c in s[0:4]): return v(s[0])
	if allsame(v(c) for c in s[1:5]): return v(s[1])
	return 0

def _fh(s):
	found=False
	for i in range(3):
		if v(s[i])==v(s[i+1])==v(s[i+2]):
			found=True
			res=v(s[i])
			break
	if not found: return 0
	x=s[0:i]+s[i+3:]
	if v(x[0])==v(x[1]): return res*100+v(x[1])
	return 0

def _fl(s):
	if not allsame(u(c) for c in s): return 0
	return v(s[4])

def _st(s):
	if not increasing(v(c) for c in s): return 0
	return v(s[4])

def _tk(s):
	if allsame(v(c) for c in s[0:3]): return v(s[0])
	if allsame(v(c) for c in s[1:4]): return v(s[1])
	if allsame(v(c) for c in s[2:5]): return v(s[2])
	return 0

def _tp(s):
	found=False
	for i in range(4):
		if v(s[i])==v(s[i+1]):
			found=True
			break
	if not found: return 0
	x=s[0:i]+s[i+2:]
	for j in range(2):
		if v(x[j])==v(x[j+1]):
			return v(x[j])
	return 0

def _op(s):
	if allsame(v(c) for c in s[0:2]): return v(s[0])
	if allsame(v(c) for c in s[1:3]): return v(s[1])
	if allsame(v(c) for c in s[2:4]): return v(s[2])
	if allsame(v(c) for c in s[3:5]): return v(s[3])
	return 0

def _hc(s):
	return v(s[4])

def cmp(s1, s2):
	fns=[_rf, _sf, _fk, _fh, _fl, _st, _tk, _tp, _op, _hc]
	for fn in fns:
		f1=fn(s1)
		f2=fn(s2)
		print 'fn {} f1={} f2={}'.format(fn.__name__, f1,f2)
		if f1!=0 and f2==0: return 'a'
		if f1==0 and f2!=0: return 'b'
		if f1!=0 and f2!=0:
			if f1>f2: return 'a'
			if f2>f1: return 'b'
			v1=sum(100**i * v(c) for i,c in enumerate(s1))
			v2=sum(100**i * v(c) for i,c in enumerate(s2))
			print 'fn {} v1={} v2={}'.format(fn.__name__, v1,v2)
			if v1>v2: return 'a'
			if v2>v1: return 'b'
	return 'c'

awin=0
for s in ss:
	s[0:5]=sorted(s[0:5],key=lambda c:v(c)*1000+ord(c[1]))
	s[5:10]=sorted(s[5:10],key=lambda c:v(c)*1000+ord(c[1]))
	cc=cmp(s[:5], s[5:])
	if cc == 'c': raise ValueError()
	if cc == 'a': awin+=1
print awin
