x = int(input("Enter your marks"))

if (x<0 or x>100):
    print("Enter valid marks")
else:
    while (x<=100):
        if (x>=90):
            print("Your grade is A+")
        elif (80 <= x <90):
            print("Your grade is A")
        elif (70 <= x <80):
            print("Your grade is B")
        elif (60 <= x <70):
            print("Your grade is C")
        elif (50 <= x <60):
            print("Your grade is D")
        else:
            print("Fail")
        break
