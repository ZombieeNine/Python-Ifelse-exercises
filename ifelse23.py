x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))
x3=int(input("x3:"))
y3=int(input("y3:"))

if x1==x2:
    x4=x3
if y1==y3:
    y4=y2
else:
    y4=y1
if x1==x3:
    x4=x2
if y1==y2:
    y4=y3
else:
    y4=y1
if x1!=x2:
    x4=x1
if y2==y3:
    y4=y1
else:
    y4=y2

print("Координаты четвертой вершины:",x4,y4)
