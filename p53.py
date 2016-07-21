from math import factorial as f
print sum(f(n)/f(r)/f(n-r)>1000000 for n in range(1,101) for r in range(0, n+1))