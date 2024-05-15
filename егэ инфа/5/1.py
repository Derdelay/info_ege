for n in range(1,128):
    n2=bin(n)[2:].zfill(8)
    n2=n2.replace('0','2').replace('1','0').replace('2','1')
    n2=int(n2,2)+1
    if n2 ==153:
        print(n)