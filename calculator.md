print("Choose the Operation:")
print("Enter 1 for Addition(+)")
print("Enter 2 for Subtraction(-)")
print("Enter 3 for Multiplication(*)")
print("Enter 4 for Division(\)")

operation=int(input("Enter the operation you want to apply:"))

try:
    num1=float(input("Enter the First Number:"))
    num2=float(input("Enter the Second Number:"))
    
    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    else:
        print("Invalid Operation please enter the valid operation.")    
                  
except ZeroDivisionError:
    print("Number can't be divided by 0 ")     
    
except ValueError:
    print("Enter the valid input")           

        
        
