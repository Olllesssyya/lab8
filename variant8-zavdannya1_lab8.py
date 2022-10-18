#Лабароторна 8 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab8

from array import *
import random
import math
s = 1
c = 0

N=int(input("Задайте кількість елементів масиву: "))
arr=array('i',[])

for i in range(N):
    x=random.randint(0,10)
    arr.append(x)

print(arr)

for j in arr:
    if j%2==0:
        print("парний елемент =",j)
        s=s*j
        c+=1
           
if c>0:
    print("Середнє геометричне дорівнює: ",math.pow(s, (1/c)))
else:
    print("Масив не містить парних чисел")
    

