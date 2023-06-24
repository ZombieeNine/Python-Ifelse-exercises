import random

d=random.randrange(1,32)
m=random.randrange(1,13)
if m==2:
    d=random.randrange(1,29)
print("Дата:")
print(f"Месяц: {m}. День: {d}")
if d > 1:
    d -= 1
else:
    if m == 1:
        m = 12
    else:
        m -=1
print("Предыдущая дата:")
print(f"Месяц: {m}. День: {d}")
