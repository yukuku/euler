nn=open('p022_names.txt').read().replace('","',' ').replace('"','').split()
print sum(sum(ord(c)-64 for c in n) * (i+1) for i, n in enumerate(sorted(nn)))
