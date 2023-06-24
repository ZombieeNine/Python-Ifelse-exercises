import random

d=int(random.randrange(1,32))
m=int(random.randrange(1,13))
if m==2:
    d=random.randrange(1,29)
print("Дата:")
print(f"Месяц: {m}. День: {d}")
if d < d+1:
    d += 1
else:
    d = 1
    if m == 12:
        m = 1
    else:
        m +=1
print("Следующая дата:")
print(f"Месяц: {m}. День: {d}")