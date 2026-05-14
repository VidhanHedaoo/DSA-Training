# function is a self excuteable block that executes whenever we want 

# def hello(): #called function
#     print("hello there!")

# hello() #calling function  

# ----------------------------------------------------------

# def arithmetic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))

#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul  #return in a form of tuple and not a list bcoz the return value is not going to change in runtime  
#     #it is possible to return multiple values in python function


# # print(arithmetic())
# result = arithmetic()
# print("Arithmetic =",result)

# -----------------------------------------------------------

#positional argument 

# def arithmetic(a, b):

#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul

# #positional argument ,here left to right the positions are fixed.
# result = arithmetic(5, 5)
# print("Arithmetic =",result)

# ----------------------------------------------------------

# keyword argument

# def credential(username, password):
#     if username == password:
#         print("Login succesful.")
#     else:
#         print("Invalid credentials!")

# credential(username="admin",password="admin") #calling function

# ----------------------------------------------------------

#default argument

# def cityName(city="Pune"):
#     print(city)

# cityName("Nagpur")
# cityName("Mumbai")
# cityName()  # here no value(arg) is passed so prints the default value pune 

# ---------------------------------------------------------

# variable length argument / variable number of arguments

# def cityName(*name): # just like sql to select all args we use * as a prefix which takes no.of args at a time as a tuple 
#     print(name)

# cityName("Nagpur","delhi","Mumbai","pune")    

