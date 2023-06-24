print("1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер")
a = int(input("Номер единицы массы: "))
m = float(input("Масса: "))
if a == 1:
    print(" кг")
    m = m
elif a == 2:
    print(" мг")
    m = m / 1000000
elif a == 3:
    print(" г")
    m = m / 1000
elif a == 4:
    print(" т")
    m = m * 1000
elif a == 5:
    print(" ц")
    m = m * 100
print("В килограммах: ",m)