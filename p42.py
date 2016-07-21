tn=set((n*n+n)/2 for n in range(1,100))
ww=open('p042_words.txt').read().replace('"','').split(',')
print sum(sum(ord(c)-64 for c in w) in tn for w in ww)
