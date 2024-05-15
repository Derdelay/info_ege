r=0
for t in range(4,10000):
    n='3'+'5'*t
    while ('555'in n) or ('333'in n):
        if '555' in n:
            n=n.replace('555','3')
        else:
            n=n.replace('333','5')
    r3=n.count('3')*3
    r5=n.count('5')*5
    if (r3+r5)>r:
        r=(r3+r5)
print(r)