import random
x=random.randrange(1,999)

if x%2==0:
    s="четное"
else:
    s="нечетное"
x_str=str(x)
n=len(x_str)
if n==1:
    s+="однозначное"
elif n==2:
    s+="двузначное"
elif n==3:
    s+="трехзначное"
s+="число"
print(x," : ",s)