def de(s):
	pos=0
	res=0
	while pos<len(s):
		c=s[pos]
		d=s[pos+1] if pos<len(s)-1 else ''
		if c=='M': res+=1000
		elif c=='D': res+=500
		elif c=='C':
			if d=='D': res+=400; pos+=1
			elif d=='M': res+=900; pos+=1
			else: res+=100
		elif c=='L': res+=50
		elif c=='X': 
			if d=='L': res+=40; pos+=1
			elif d=='C': res+=90; pos+=1
			else: res+=10
		elif c=='V': res+=5
		elif c=='I':
			if d=='V': res+=4; pos+=1
			elif d=='X': res+=9; pos+=1
			else: res+=1
		pos+=1
	return res

def en(n):
	res=''
	while n>=1000: res+='M'; n-=1000
	if n>=900: res+='CM'; n-=900
	if n>=500: res+='D'; n-=500
	if n>=400: res+='CD'; n-=400
	while n>=100: res+='C'; n-=100
	if n>=90: res+='XC'; n-=90
	if n>=50: res+='L'; n-=50
	if n>=40: res+='XL'; n-=40
	while n>=10: res+='X'; n-=10
	if n>=9: res+='IX'; n-=9
	if n>=5: res+='V'; n-=5
	if n>=4: res+='IV'; n-=4
	while n>=1: res+='I'; n-=1
	return res

res=0
for line in open('p089_roman.txt').readlines():
	n=de(line)
	s=en(n)
	res+=len(line.strip())-len(s)
print res
