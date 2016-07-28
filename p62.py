def canon(n): return ''.join(sorted(list(str(n))))

d={}

import itertools
for n in itertools.count():
	c=canon(n**3)
	v=d.get(c,[])+[n]
	d[c]=v
	if len(v)==5:
		print c, len(d), d[c], min(d[c]), min(d[c])**3
		break
