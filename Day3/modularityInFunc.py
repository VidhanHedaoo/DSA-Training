#modularity  in function
import sys

def add():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    print(a+b)

def sub():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    print(a-b)

def div():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    print(a/b)

def mul():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    print(a*b)    

#menu driven system
             
while(True):
    print("1.Addition")
    print("2.Substraction")
    print("3.division")
    print("4.multiplictaion")
    print("5.exit")  

    choice = int(input("Enter your choice :"))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        div()
    elif choice == 4:
        mul()
    elif choice == 5: 
        sys.exit()  #we would have used break statement here 




    