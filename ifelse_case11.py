import random

d = {'С' : 'Север', 'З' : 'Запад', 'Ю' : 'Юг', 'B' : 'Восток'}
r = {-1 : "поворот направо", 2 : "поворот на 180 градусов", 1 : "поворот налево"}
d1 = {0 : 'С', 1: 'З',  2 : 'Ю', 3 : 'B'}
i = int(input("Исходное направление(0-Север, 1-Запад, 2-Юг, 3-Восток): "))
C = d[d1[i]]
print("Исходное направление: ", C)
N1 = int(input("Первая команда(-1-поворот направо, 2-поворот на 180 градусов, 1-поворот налево): "))
print("Поворот: ", r[N1])
if N1 == -1:
    if i == 0:
        i = 3
    elif i == 3:
        i = 2
    elif i == 2:
        i = 1
    elif i == 1:
        i == 0
elif N1 == 1:
    if i == 0:
        i = 1
    elif i == 1:
        i = 2
    elif i == 2:
        i = 3
    elif i == 3:
        i = 0
elif N1 == 2:
    if i==0:
        i=2
    elif i==1:
        i=3
    elif i==2:
        i=0
    elif i==3:
        i=1
C = d[d1[i]]
print("Первое направление : ", C)
N2 = int(input("Вторая команда(-1-поворот направо, 2-поворот на 180 градусов, 1-поворот налево): "))
print("Поворот: ", r[N2])
if N2 == -1:
    if i == 0:
        i = 3
    elif i == 3:
        i = 2
    elif i == 2:
        i = 1
    elif i == 1:
        i == 0
elif N2 == 1:
    if i == 0:
        i = 1
    elif i == 1:
        i = 2
    elif i == 2:
        i = 3
    elif i == 3:
        i = 0
elif N2 == 2:
    if i==0:
        i=2
    elif i==1:
        i=3
    elif i==2:
        i=0
    elif i==3:
        i=1
C = d[d1[i]]
print("Второе направление : ", C)