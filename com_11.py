totalClassesHeld = eval(input("Enter total number of classes held in school : "))

totalClassesAttend = eval(input("Enter total number of classes attended by the student : "))
atten = (totalClassesAttend/float(totalClassesHeld))*100
print("Attendence is",atten)
medical_cause=input("Medical cause? Y or N:\n")

if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")
