quantity=int(input("Enter quantity:\n"))
if quantity>1000:
    print("Cost is",((quantity*100)-(.1*quantity*100)))
else:
    print("Cost is",quantity*100)
