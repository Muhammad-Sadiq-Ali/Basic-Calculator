import math 
# By taking a new variable as flag help to automatically restart the program whenever the value of flag is true.
flag = True
while flag == True:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    operator = input("Enter the function you have to performed(-,+,/,//,**,*,ceil, %, x!, y!) : ")
    if operator == "+":
        print("The sum is : ",x+y)
    elif operator == "-":
        print("The difference is : ", x-y)
    elif operator == "*":
        print("The product is : ", x*y)
    elif operator == "**":
        print("The power is : ", x**y)
    elif operator == "//":
        # when y =0, there will be an error in output stating that denominator can't be zero.
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The answer rounded down to is : ",x//y)
        else :
            print("The answer rounded down is : ",x//y)
    elif operator == "ceil":
        # when y =0, there will be an error in output stating that denominator can't be zero.
        if y == 0:
            print("Error! The denominator can't be zero.")
            y = int(input("Enter second number : "))
            if y!=0:
                print("The rounded up to is : ", math.ceil(x/y))
        else :
            print("The answer rounded up is : ",math.ceil(x/y))
    elif operator == "%":
        # when y =0, there will be an error in output stating that denominator can't be zero.
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
    elif operator == "x!":
        if x>0:
            v = 1
            for i in range(1, x+1):
                v *=i 
            print("The factorial of first number is : ", v)
        elif x==0:
            print("The factorial of first number is 0.")
        else:
            print("The factorial of negative number doesn't exist.")
    elif operator == "y!":
        if y>0:
            z = 1
            for i in range(1, y+1):
                z *=i 
            print("The factorial of second number is : ", z)
        elif y==0:
            print("The factorial of second number is 0.")
        else:
            print("The factorial of negative number doesn't exist.")
    else:
        print("type the correct operator.")
    # In "c" variable, we will store whether user want to restart the program or not. when value of "c" is yes, The program will restart. 
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

     
