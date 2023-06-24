import math

x=float(input("X:"))
x_floor = math.floor(x)
if x<0:
    f=0
    print(f"x = {x} : f(x) = {f}")
elif x_floor%2==0:
    f=1
    print(f"x = {x} : f(x) = {f}")
else:
    f=-1
    print(f"x = {x} : f(x) = {f}")
