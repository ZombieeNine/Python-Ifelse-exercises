a=int(input("a:"))
b=int(input("b:"))
if a!=b:
    a=b=a+b
else:
    a=b=0
print(f"A:{a}", f"B:{b}")