s=''.join(str(n) for n in range(1, 1000001))
print reduce(lambda a,b: a*b, [int(s[10**n-1]) for n in range(7)], 1)
