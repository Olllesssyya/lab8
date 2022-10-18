#Лабароторна 8 варіант 8 завдання 2. Посилання на GitHub https://github.com/Olllesssyya/Lab8
import numpy as np

m = int(input("Введіть кількість строк масиву: "))
n = int(input("Введіть кількість стовпчикив масиву: "))

a=np.random.randint(1, 30, size = (m, n))
b=np.random.randint(31, 50, size = (m, n))

c=a+b

print("масив а:",a)
print("масив b:",b)
print("масив с:",c)

print("Сума стовпчиків масиву С: ",c.sum(axis=0))
d=c[:,np.argmin(c.sum(axis=0))]
print("Стовпчик, сума елементів, яка найменша: ", d)

