def calculator():
    try:
        print("\n-----Calculator-----")
        print("\nChoose the Operation")
        print("\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
        choice = int(input("\nEnter the Choice : "))
        num1 = float(input("Enter the First Number : "))
        num2  = float(input("Enter the Second Number : "))
        if choice == 1:
            print(f"Addition of {num1} and {num2} is : ", num1+num2)
        elif choice == 2:
            print(f"Subtraction of {num1} and {num2} is : ", num1-num2)
        elif choice == 3: 
            print(f"Multiplication of {num1} and {num2} is : ", num1*num2)
        elif choice == 4:
            if num2==0:
                print("Value is undefined")
            else:
                print(f"Division of {num1} and {num2} is : ", num1/num2)
        else:
            print("Invalid option Entered")
    except:
        print("invalid input !, Please enter a valid input")
def tables():
    try:
        print("\n-----Tables Generator-----")
        num = int(input("Enter the Number : "))
        limit = int(input("Enter the Range of the Tables : "))
        print(f"Multiplication Table of {num} is : ")
        for i in range(1, limit+1):
            print(f"{num} x {i} = {num*i}")
    except:
        print("Invalid Input !")
while True:
    print("-----MENU-----")
    print("\n1. Calculator")
    print("2. Tables Generator")
    print("3. Exit")
    choice1 = int(input("Enter your Choice : "))
    if choice1 == 1:
        calculator()
    elif choice1 == 2:
        tables()
    elif choice1 == 3:
        print("Exiting the Application....")
        break
    else:
        print("Invalid Choice Entered")  
                      


                   



