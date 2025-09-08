import math
#Extended Calculator
print("Welcome to my extended Calculator!")
print("This calculator can perform Square root, nth root and PIE calculation")
while True:
    print("Choose your operation for today")
    print("1. Square root")
    print("2. nth Root")
    print("3. PIE")
    print("4. Exit")
    choice = input("Enter your option (1/2/3/4)")
    if choice == "1":
        num = float(input("Enter a number"))
        if num>=0:
            result = math.sqrt(num)
            print("The square root is",result)
        else:
            print("error")
    elif choice ==  "2":
        num = float(input("Enter a number"))
        n = float(input("Enter root degree(eg., 2 for square root, 3 for cube root)"))
        if n!=0:
            result = num**(1/n)
            print(f"The{n}th root{num} is:",result)
        else:
            print("Error")
    elif choice =="3":
        print("The value of pi is",math.pi)
    elif choice =="4":
        print("Goodbye!")
        break
else:
    print("Error")
    



