units=int(input("Enter units:\n"))
if units<=100:
    print("No charge")
elif units>100 and units<=200:
    rs=(units-100)*5
    print("Total bill amount is Rs",rs)
elif units>200:
    rs=(units-100)*10
    print("Total bill amount is Rs",rs)
