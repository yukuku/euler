def pal(n):
	s = str(n)
	return s == s[::-1]

print max(i*j for i in range(100, 1000) for j in range(100, 1000) if pal(i*j))
