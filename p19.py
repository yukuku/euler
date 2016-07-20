mn=[31,28,31,30,31,30,31,31,30,31,30,31]
ml=mn[:]
ml[1]=29

#1901-1-1 is tue. sun==0
fd=2
res = 0
for y in range(1901,2001):
	mm = ml if y%4==0 else mn
	for bul in range(12):
		if fd==0: res+=1
		fd = (fd+mm[bul])%7
print res
