n = int(input("Enter your marks"))

if (n<0 or n>100):
    print("Enter valid marks")
else:
    while (n<=100):
        if (n>=90):
            print("Your grade is A+")
        elif (80 <= n <90):
            print("Your grade is A")
        elif (70 <= n <80):
            print("Your grade is B")
        elif (60 <= n <70):
            print("Your grade is C")
        elif (50 <= n <60):
            print("Your grade is D")
        else:
            print("Fail")
        break
