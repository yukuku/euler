pp=[n*(3*n-1)/2 for n in range(1,10000)]
ps=set(pp)
print min(pp[k]-pp[j] for j in range(len(pp)) for k in range(j+1,len(pp)) if (pp[j]+pp[k]) in ps and (pp[k]-pp[j]) in ps)
