import math 
flag = True
while flag == True:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    operator = input("Enter the function you have to performed(-,+,/,//,**,*,ceil, %) : ")
    if operator == "+":
        print("The sum is : ",x+y)
    elif operator == "-":
        print("The difference is : ", x-y)
    elif operator == "*":
        print("The product is : ", x*y)
    elif operator == "**":
        print("The power is : ", x**y)
    elif operator == "//":
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The answer rounded down to is : ",x//y)
        else :
            print("The answer rounded down is : ",x//y)
    elif operator == "ceil":
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The rounded up to is : ", math.ceil(x/y))
        else :
            print("The answer rounded up is : ",math.ceil(x/y))
    elif operator == "%":
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The remainder or modulus is : ",x%y)
        else :
            print("The remainder or modulus is : ",x%y)
    elif operator == "/":
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The ratio is : ",x/y)
        else : 
            print("The ratio is : ", x/y)
    else:
        print("type the correct operator.")
    c = input("Do you want to continue  (yes or no) : ")
    if c == "yes":
        flag = True
    elif c == "no" : 
        flag = False
        print("Thank You!!")
    else:
        print("To continue, type 'yes' and to terminate, type 'no'.")
        c = input("yes or no : ")
        if c!= "yes":
            print("Thank You!!")
            flag = False
        elif c=="yes":
            flag = True

     