a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if abs(a-b) < abs(a-c):
    print("point b", f"distance {abs(a-b)}")
else:
    print("point c", f"distance {abs(a-c)}")
