n='8'*99+'1'
while '133' in n or '881' in n:
    if '133' in n:
        n=n.replace('133','81',1)
    else:
        n=n.replace('881','13',1)
print(n)