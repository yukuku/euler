jw={}
def s(x,y):
	if x==0 or y==0: return 1
	res = jw.get((x,y), 0)
	if res: return res
	res = s(x-1,y)+s(x,y-1)
	jw[(x,y)] = res
	return res

print s(20,20)
