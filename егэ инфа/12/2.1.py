for n in range(1000):
    s='>'+39*'0'+n*'1'+39*'2'
    while ('>1' in s) or ('>2' in s) or ('>0' in s):
        if '>1' in s:
            s=s.replace('>1', '22>')
        if '>2' in s:
            s=s.replace('>2', '2>')
        if '>0' in s:
            s=s.replace('>0', '1>')
        l=s.count('2')*2+s.count('1')
    k=0
    for i in range(1, l+1):
        if l % i == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        print(n)
        break