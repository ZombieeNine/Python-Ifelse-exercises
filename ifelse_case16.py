import random

desyatki = {
    20 : 'двадцать',
    30 : 'тридцать',
    40 : 'сорок',
    50 : 'пятьдесят',
    60 : 'шестьдесят'}
edinici  = {
    1 : 'один год',
    2 : 'два года',
    3 : 'три года',
    4 : 'четыре года',
    5 : 'пять лет',
    6 : 'шесть лет',
    7 : 'семь лет',
    8 : 'восемь лет',
    9 : 'девять лет'}

N = random.randrange(20,70)
print("N = ",N)
r = N%10
if r == 0:
    print("{0} лет".format(desyatki[N]))
else:
    q = int(N/10)*10
    print("{0} {1}".format(desyatki[q], edinici[r]))
