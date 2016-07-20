t = [[int(c) for c in l.split()] for l in open('p067_triangle.txt').read().splitlines()]

nr = len(t)
jw = {}

def m(r, c):
	if r+1 == nr: return t[r][c]
	if (r,c) in jw: return jw[(r,c)]
	res = t[r][c] + max(m(r+1,c), m(r+1,c+1))
	jw[(r,c)] = res
	return res

print m(0,0)
