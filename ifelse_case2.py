# k=int(input("K:"))
# if k<1 or k>5:
#     print("ошибка")
# if k==1:
#     print("плохо")
# elif k==2:
#     print("неудовлетворительно")
# elif k==3:
#     print("удовлетворительно")
# elif k==4:
#     print("хорошо")
# elif k==5:
#     print("отлично")

osenka={
    1 : "плохо",
    2 : "неудовлетворительно",
    3 : "удовлетворительно",
    4 : "хорошо",
    5 : "отлично"}
k=int(input("K:"))
if k in range(1,6): print("Ваша оценка: ", osenka[k].capitalize() )
else: print("ошибка")