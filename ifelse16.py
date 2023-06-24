a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
if a<b<c:
    a=a*2
    c=c*2
    b=b*2
else:
    a=a*(-1)
    b=b*(-1)
    c=c*(-1)
print (f"A:{a}", f"B:{b}", f"C:{c}")