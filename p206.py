import math

#1_2_3_4_5_6_7_8_9_0

mis=1020304050607080900
mas=1929394959697989990

for n in xrange(int(math.sqrt(mis))/10*10, int(math.sqrt(mas))+1, 10):
	dn=n/10%10
	if dn==3 or dn==7:
		n/=10
		ns=n*n
		s=str(ns)
		if s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8':
			print n*10, ns*100
