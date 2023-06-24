year=int(input("Year:"))


if (year%4==0) and not(year%100==0 and year%400!=0):
    print(year,"is leap year." )
else:
    print(year,"is normal year.")