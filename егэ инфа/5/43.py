for n in range(1000):
    n2=bin(n)[2:]
    n2=n2+str(n2.count('1')%2)
    n2=n2+str(n2.count('1')%2)
    print(int(n2,2))

