import random

sotni={
    100 : "сто",
    200 : "двести",
    300 : "тристо",
    400 : "четыресто",
    500 : "пятьсот",
    600 : "шестьсот",
    700 : "семьсот",
    800 : "восемьсот",
    900 : "девятьсот",}
desyatki = {
    10 : 'десять',
    20 : 'двадцать',
    30 : 'тридцать',
    40 : 'сорок',
    50 : 'пятьдесят',
    60 : 'шестьдесят',
    70 : 'семьдесят',
    80 : 'восемьдесят',
    90 : 'девяносто'}
dcat = {
    11 : 'одиннадцать',
    12 : 'двенадцать',
    13 : 'тринадцать',
    14 : 'четырнадцать',
    15 : 'пятнадцать',
    16 : 'шестнадцать',
    17 : 'семнадцать',
    18 : 'восемнадцать',
    19 : 'девятнадцать',}
edinici  = {
    1 : 'один',
    2 : 'два',
    3 : 'три',
    4 : 'четыре',
    5 : 'пять',
    6 : 'шесть',
    7 : 'семь',
    8 : 'восемь',
    9 : 'девять'}

N = random.randrange(100,1000)
print("N = ",N)
itog = ''
q = int(N/100)*100
itog += sotni[q]
N -= q 
if 10 < N and N < 20:
    itog += ' ' + dcat[N]
else:
    r = N%10
    q = int(N/10)*10
    if q !=0:
        itog += ' ' + desyatki[q]
    if r != 0:
        itog += ' ' + edinici[r]

    print(itog)