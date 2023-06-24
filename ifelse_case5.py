print("1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление")
n=int(input("Введите номер действия:"))
a=float(input("A:"))
b=float(input("B:"))
if b<0:
    b_str="("+str(b)+")"
else:
    b_str=str(b)
if n==1:
    print(a,"+",b_str,"=", a+b)
elif n==2:
    print(a,"-",b_str,"=", a-b)
elif n==3:
    print(a,"*",b_str,"=", a*b)
elif n==4:
    if b==0:
        print("Деление на ноль неопределено")
    else:
        print(a,"/",b_str,"=", a/b)