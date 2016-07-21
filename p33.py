def same(aa,bb,c,d):
	return aa*d == bb*c

def cb(aa,bb):
	ax, ay = aa/10, aa%10
	bx, by = bb/10, bb%10
	if ax==bx and same(aa,bb,ay,by): return True
	if ax==by and same(aa,bb,ay,bx): return True
	if ay==bx and same(aa,bb,ax,by): return True
	if ay==by and same(aa,bb,ax,bx): return True
	return False

jw = [(aa, bb) for aa in range(10, 100) if aa%10!=0 for bb in range(aa+1, 100) if bb%10!=0 if cb(aa,bb)]
prod = (jw[0][0]*jw[1][0]*jw[2][0]*jw[3][0], jw[0][1]*jw[1][1]*jw[2][1]*jw[3][1])
print prod
