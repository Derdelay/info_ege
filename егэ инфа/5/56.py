def IsPrime(n):
    d = 2
    while d **2 <= n and n % d != 0:
        d += 1
    return d * d > n
print(IsPrime(int(23)))