'''def f(a,b,m): #a=кол-в камней в 1 куче,b=кол-во во 2 куче, m=кол-во ходов
    if a+b>45#условие окончания игры:  return m%2==0  
    if m==0:    return 0
    h = [f(a+1,b,m-1),f(a*3,b,m-1),f(a,b+1,m-1),f(a,b*3,m-1)] #доступные дейстия
    return any(h) if (m-1)%2==0 else all(h) #если первый ход должен быть неудачный all->any
print([s for s in range(1,41#1<=s<=40)if f(4,s,2)])#f(начальный момент в1куче,во2куче,номер хода)])#19 задание
print([s for s in range(1,41)if not f(4,s,2) and f(4,s,3)]) #20 задание
print([s for s in range(1,41)if not f(4,s,2) and f(4,s,4)]) #21 задание
'''