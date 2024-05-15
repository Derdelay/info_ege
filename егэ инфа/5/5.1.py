n=25
n2=bin(n)[2:]
r=n2+str(int(n2.count('1'))%2)
r=r+str(int(r.count('1'))%2)
print(int(r,2))
