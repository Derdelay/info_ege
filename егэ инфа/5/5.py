#  for n in range(1000):
#двоичная запись числа N. n2=bin(n)[2:]
#подсчёт цифр 1. n=n2.count('1')
#вычет поседних двух знаков n2=n2[:-2]
#нахождение знака по порядку n2[0]-первый знак n2[-1]-последний знак
#удаление знака del n2[0]
#n2=n2.replace('1','2') замена 1 на 2
#.zfill(8) заполнить строку до 8-ми символов
"""
def IsPrime(n):
    d = 2
    while d **2 <= n and n % d != 0:
        d += 1
    return d * d > n
print(IsPrime(int()))
"""#определение простого числа

'''from turtle import *
speed(100000)
k=20
right(45)
for i in range(7):
    right(45)
    forward(10*k)
    right(135)
    back(3)
penup()
for x in range(-1,30):
    for y in range(-15,5):
        setpos(x*k,y*k)
        dot(4,'black')
tracer(0)
done()
        '''#исполнитель черепаха


'''
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
'''#Функция перевода чисел в произвольную систему счисления на Python
