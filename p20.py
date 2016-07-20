f=reduce(lambda a,b: a*b, range(1,101), 1)
print sum(ord(c)-48 for c in str(f))
