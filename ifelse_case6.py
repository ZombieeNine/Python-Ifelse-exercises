print("1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр")
dlina={
    1 : "дм",
    2 : "км",
    3 : "м",
    4 : "мм",
    5 : "см"}
a=int(input("Номер единицы длины: "))
n=float(input("Длина: "))
print(n,dlina[a])
if a in [1]: print("В метрах: ",n/10)
elif a in [2]: print("В метрах: ",n*1000)
elif a in [3]: print("В метрах: ",n)
elif a in [4]: print("В метрах: ",n/1000)
elif a in [5]: print("В метрах: ",n/100)