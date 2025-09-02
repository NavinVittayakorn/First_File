print("welcome to my fully functional calculator")
print("select your operation")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Devide")
choice = input("Enter your choice (1/2/3/4)")
num1 = float(input("Enter your first value"))
num2 = float(input("Enter your second value"))
if choice =="1":
    Result = num1+num2
    print("The sum is", Result)
elif choice =="2":
    Result = num1-num2
    print("The difference is", Result)
elif choice =="3":
    Result = num1*num2
    print("The product is", Result)
elif choice =="4":
    if num2 != 0:
        Result = num1/num2
        print("The quotient is", Result)
    else:
        print("Error, cannot be devide by zero")
else:
    print("Invalid value")

