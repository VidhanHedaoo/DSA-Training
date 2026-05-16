# def func(value, values): #address of v is passed here,
#     var =1 
#     values[0]= 44 # so any changes in values also means changes in v as well

# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0]) #Output -> 3 44

# ----------------------------------------

# def f(i,values =[]):
#     values.append(i)
#     print(values)

# f(1)
# f(2)
# f(3)

# Output 
'''[1]
   [1, 2]
   [1, 2, 3]'''
# --------------------------------------------

# fruit = {}
# def addon(index):
#    if index in fruit:
#       fruit[index] += 1
#    else:
#       fruit[index] = 1

# addon('Apple')
# addon('Banana')
# addon('apple')

# print(len(fruit)) #3
# --------------------------------------------


# val = [2**i for i in range(1,6)] # for loop compressed with condition # 2**i = i^2
# print(val)

# s = [i*i for i in range(1,6)] # for loop compressed with condition for finding squares
# print(s)

# --------------------------------------------
# squares = {x:x*x for x in range(1,6)} #dictionary comprehension
# print(squares)
# -----------------------------------------------------

# double = {x:2*x for x in range(1,6)}
# print(double)
# -----------------------------------------------------

# a,b = [int(x) for x in input("enter the number: ").split()] #taking multiple values in single line
# print("Product is : ", a*b)
# ----------------------------------------------------

# a,b,c = [float(x) for x in input("Enter 3 flost numbers: ").split(',')]
# print("The sum is : ", a+b+c)

'''Enter 3 flost numbers: 2.3,4.5,6.7
   The sum is :  13.5'''

# ------------------------------------------------------
# we can use else block with for loop

# cart = [10,20,800,40,60]
# for item in cart:
#    if item >400:
#       print("This is not in budget.")
#       continue
#    print(item)
# else:
#    print("you have purchased everything.")   

# --------------------------------------------------

#username and password should be  same otherwise ask again infinetrly

username = "admin"
password = "admin"

while True:
   u = input("Enter username: ")
   p = input("Enter password: ")

   if u == username and p == password:
      print("Login succesful!")
      break
   else:
      print("Incorrect credentials. Try again.")   