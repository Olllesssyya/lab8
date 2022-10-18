#Лабароторна 8 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab8
from array import *
import random
import math
s = 0
c = 0

N=int(input("Задайте кількість елементів масиву: "))
arr=array('i',[])

for i in range(N):
    x=random.randint(0,10)
    arr.append(x)
    print(arr[i])

for j in arr:
    if j%2==0:
        print("J=",j)
        if s>0:
            s=s*j
            c+=1
        else:
            s=j
            c+=1   
print("Середне геометричне дорівнює: ",math.pow(s, (1/c))) #корінь з s в ступені с
print(c)