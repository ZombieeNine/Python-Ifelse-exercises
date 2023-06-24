import random
import math

r = {1 : "радиус R", 2 : "диаметр D", 3 : "длина L", 4 : "площадь круга S"}
c = []

i = int(input("1=радиус R, 2=диаметр D, 3=длина L, 4=площадь круга S: "))
N = random.randrange(1,100)
print(r[i],":",N)
if i == 1:
    R = N
    D=(2 * R)
    L=(2 * math.pi * R)
    S=(math.pi * R**2)
elif i == 2:
    D = N
    R = D / 2
    L=(math.pi * D)
    S=(math.pi * R**2)
elif i == 3:
    L = N
    R = L / 2 / math.pi
    D=(2 * R)
    S=(math.pi * R**2)
elif i == 4:
    S = N
    R = math.sqrt(S / math.pi)
    D=(2 * R)
    L=(2 * math.pi * R)

c.append(R)
c.append(D)
c.append(L)
c.append(S)

print()
print("Элементы окружности:")
for i in range(0,4):
    print(r[i+1],":",c[i])