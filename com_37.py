text = input("Enter a string: ")
text = text.strip()
if len(text) < 1:
    print("Enter a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    else:
        print("The string is not an integer.") 
