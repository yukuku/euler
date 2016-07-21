def t(n):
	ss = [str(k*n) for k in range(1,7)]
	return set(ss[0]) == set(ss[1]) == set(ss[2]) == set(ss[3]) == set(ss[4]) == set(ss[5])

def main():
	ms = [10**i for i in range(1, 7)]
	for m in ms:
		for n in range(m/10, m/6+1):
			if t(n):
				print n,2*n,3*n,4*n,5*n,6*n
				return
main()
