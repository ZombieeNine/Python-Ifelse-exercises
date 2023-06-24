print("1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр")
a=int(input("Номер единицы длины: "))
n=float(input("Длина: "))
if a==1:
    print(" дм")
    print("В метрах: ",n/10)
elif a==2:
    print(" км")
    print("В метрах: ",n*1000)
elif a==3:
    print(" м")
    print("В метрах: ",n)
elif a==4:
    print(" мм")
    print("В метрах: ",n/1000)
elif a==5:
    print(" см")
    print("В метрах: ",n/100)