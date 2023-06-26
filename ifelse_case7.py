print("1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер")
ves={
    1 : "кг",
    2 : "мг",
    3 : "г",
    4 : "т",
    5 : "ц"}
a = int(input("Номер единицы массы: "))
m = float(input("Масса: "))
print(m,ves[a])
if a in [1]: m = m
elif a in [2]: m = m / 1000000
elif a in [3]: m = m / 1000
elif a in [4]: m = m * 1000
elif a in [5]: m = m * 100
print("В килограммах: ",m)