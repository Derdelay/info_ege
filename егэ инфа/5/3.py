n=1000000000
r2=0
while r2<=1987653210:
    n+=1
    nost=bin(n%4)[2:]
    n2=bin(n)[2:]
    r=n2+nost
    r2=int(r,2)
    if r2>=1100000000:
        print(r2)

