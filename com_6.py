num=int(input("Enter the Number:\n"))
last_digit=num%10
if(last_digit%3==0):
    print("{} is divisible by 3")
else:
    print("{} is not divisible by 3") 
