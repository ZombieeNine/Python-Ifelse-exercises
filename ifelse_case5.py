print("1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление")
deystvie={
    1 : "сложение",
    2 : "вычитание",
    3 : "умножение",
    4 : "деление"}
n=int(input("Введите номер действия:"))
a=float(input("A:"))
b=float(input("B:"))
if b<0:
    b_str="("+str(b)+")"
else:
    b_str=str(b)
if n in [1]: print(a,"+",b_str,"=", a+b)
elif n in [2]: print(a,"-",b_str,"=", a-b)
elif n in [3]: print(a,"*",b_str,"=", a*b)
elif n in [4]:
    if b==0: print("Деление на ноль неопределено")
    else: print(a,"/",b_str,"=", a/b)