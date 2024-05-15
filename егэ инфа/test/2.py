for n in range(100,1000):
    n=str(n)
    r1=int(n[0])*int(n[1])
    r2=int(n[1])*int(n[2])
    if int(str(min(r1,r2))+str(max(r1,r2)))==621:
        print(n,str(min(r1,r2))+str(max(r1,r2)))
