m=[[int(c) for c in line.split(',')] for line in open('p081_matrix.txt').readlines()]
nr, nc = len(m), len(m[0])
for r in reversed(xrange(nr)):
	for c in reversed(xrange(nc)):
		if r+1==nr and c+1==nc: continue
		if r+1==nr: m[r][c]+=m[r][c+1]
		elif c+1==nc: m[r][c]+=m[r+1][c]
		else: m[r][c]+=min(m[r+1][c],m[r][c+1])
print m[0][0]


