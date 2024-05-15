for n in range(1000):
    n2=bin(n)[2:]
    if n % 2==0 and n>1:
        n2=n2+n2[-2]+n2[-1]
    else:
        n2='1'+n2+'0'
    r=int(n2,2)
    print(r,n)