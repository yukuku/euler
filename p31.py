c={1,2,5,10,20,50,100,200}
jw={}
def way(n):
	def w(n, m):
		if n==0: return 1
		if (n, m) in jw: return jw[(n,m)]
		res = 0
		for p in filter(lambda e: e<=m, c):
			if n-p>=0:
				res += w(n-p, p)
		jw[(n,m)] = res
		return res
	return w(n, n)

print way(200)

# 5 2
# 5 1 1
# 2 2 2 1
# 2 2 1 1 1
# 2 1 1 1 1 1
# 1 1 1 1 1 1 1

# 5 1
# 2 2 2
# 2 2 1 1
# 2 1 1 1 1
# 1 1 1 1 1 1

# 5
# 2 2 1
# 2 1 1 1
# 1 1 1 1 1


# way(1)=1
# way(2)=2  2, 1 1
# way(3)=   2 1, 1 1 1