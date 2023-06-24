import math

x=float(input("X:"))
if x>0:
    f=2*math.sin(x)
    print("Function:", f)
elif x<=0:
    f=6-x
    print("Function:", f)