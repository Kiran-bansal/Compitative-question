year=int(input("Enter the year:\n"))
if (year%400)==0 and (year%100)==0:
    print(year,"is a leap year")
elif (year%4)==0 and (year%100)!=0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")
