a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
pos=0
neg=0
if a>0:
    pos+=1
elif a<0:
    neg+=1
if b>0:
    pos+=1
elif b<0:
    neg+=1
if c>0:
    pos+=1
elif c<0:
    neg+=1
print("Positive", pos)
print("Negative", neg)