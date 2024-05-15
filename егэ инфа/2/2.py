from itertools import *
def f(w,x,y,z):
    return y and (x or z)or(not(y or z))or w #в скобках записывается выражение
for a in product([0,1], repeat=4): #repeat="количество пропусков"
    table=[(1,a[0],0,1),(a[1],1,0,a[2]),(0,0,a[3],1)] #table=[(1-я строчка),(2-я строчка) и т.д.]; a[]-пустая клетка
    if len(table)==len(set(table)):
        for i in permutations('wxyz'):
            if [f(**dict(zip(i,r))) for r in table]==[0,0,0]: # ==[числа под F]
                print(i)