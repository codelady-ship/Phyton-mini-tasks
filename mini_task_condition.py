age = int(input("add your age " ))
studyType=input("are you student?(yes,no)")

if age >=18 and studyType == "no":
    print("you shold go to millitary")
elif age >= 18 and studyType == "yes":
    print("you will go to military after graduation")
else:print("you are still student")
