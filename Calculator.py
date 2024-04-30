import math
print("Welcome to the Calculator")
name = input("What is your name? ")
print("But remember that this programme only uses basic math operations.")
print("Alright",name,", NOW YOU CAN CALCULATE")
error=False
while error==False:
    first_num=int(input("ENTER first number: "))
    operation=input("ENTER an operation: ")
    second_num=int(input("ENTER second number: "))
    if(operation=="+"):
        print(first_num+second_num)
    elif(operation=="-"):
        print(first_num-second_num)
    elif(operation=="/"):
        print(first_num/second_num)
    elif(operation=="*"):
        print(first_num*second_num)
    elif(operation=="^"):
        print(math.pow(first_num,second_num))
    elif(operation=="%"):
        print(first_num%second_num)
    else:
        print("Invalid")
        error=True




