m=[[int(c) for c in line.split(',')] for line in open('p099_base_exp.txt').readlines()]
print max((i for i in range(len(m))), key=lambda i: m[i][0]**(m[i][1]/100000.0)) + 1
