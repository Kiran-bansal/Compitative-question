totalClassesHeld = eval(input("Enter total number of classes held in school : "))

totalClassesAttend = eval(input("Enter total number of classes attended by the student : "))

percent = (totalClassesAttend / totalClassesHeld) * 100

if percent < 75:
    print(percent,"You cannot sit in the exams as your attendance is too low.")
else:
    print(percent,"You can sit in the exams as your attendance is fine.")
