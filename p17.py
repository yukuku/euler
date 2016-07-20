def s(n):
	if n < 10:
		return 'zero one two three four five six seven eight nine'.split(' ')[n]
	if n < 100:
		if n < 20:
			return 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')[n-10]
		tens = '* * twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')[n/10]
		if n%10 == 0:
			return tens
		else:
			return tens + s(n%10)
	if n == 1000: return 'onethousand'
	huns = s(n/100) + 'hundred'
	if n%100 == 0:
		return huns
	else:
		return huns + 'and' + s(n%100)

a = ''.join(s(a) for a in range(1,1001))
print len(a)
