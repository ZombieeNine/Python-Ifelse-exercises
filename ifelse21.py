x=int(input("x:"))
y=int(input("y:"))

if x==0 and y==0:
    print(0)
elif y==0 and (x>0 or x<0):
    print(1)
elif x==0 and (y>0 or y<0):
    print(2)
elif (x>0 and y>0) or (x<0 and y<0) or (x>0 and y<0) or (x<0 and y>0):
    print(3)