num1 =float(input("enter 1st number:"))
op = input("choose an operation: +,-,*,/,**0.5,**n,[],][,||")
if op=="+":
   num2=float(input("enter 2nd number:" ))
   print(f"result: {num1 + num2}")
   
elif op=="-":
    num2=float(input("enter 2nd number:" ))
    print(f"result: {num1 - num2}")
elif op=="*":
    num2=float(input("enter 2nd number:" ))
    print(f"result: {num1 * num2}")
elif op=="/":
    num2=float(input("enter 2nd number:" ))
    if num2 != 0:
        print(f"result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif op=="**0.5":
    if num1 >= 0:
        print(f"result: {num1 ** 0.5}")
    else:
        print("Error: Cannot calculate square root of a negative number.")
elif op=="**n":
    n = float(input("enter the power n: "))
    print(f"result: {num1 ** n}")
elif op=="[]":
    if num1 >= 0:
        print(f"result:{int(num1)}")   
    else : 
        print(f"result: {int(num1)-1}") 
elif op=="][":
       if num1 >= 0:
           print(f"result: {int(num1) + 1}")
       else:        
        print(f"result: {int(num1)}")
elif op=="||":
    if num1 >= 0:
        print(f"result: {num1}")
    else:
        print(f"result: {-num1}")
else:
    print("Error: Invalid operation selected.")
    


