# print(5/2) #2.5
# print(5//2) #2

# --------------------------------------
# to reverse a number 

# num = 123

# a = num % 10 # mode remainder = 3
# num =num//10 
# b = num%10 
# c = num//10

# rev = a*100 + b*10 + c*1
# print(rev)

# num = 123456 
# a = num % 10
# num = num//10 
# b = num % 10 
# num = num //10
# c= num %10
# num = num//10
# d = num % 10
# num = num//10
# e = num % 10
# f = num //10

# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f*1
# print(rev)

# ----------------------------------------

amount = int(input("Enter amount for withdrawal :")) 
print(" 100 notes = ",amount//100)
print(" 50 notes  = ",(amount%100)//50)
print(" 20 notes  = ",((amount%100)%50)//20)
print(" 10 notes  = ",(((amount%100)%50)%20)//10)
print(" 5 notes  = ",((((amount%100)%50)%20)%10)//5)
print(" 2 notes  = ",(((((amount%100)%50)%20)%10)%5)//2)
print(" 1 notes  = ",((((((amount%100)%50)%20)%10)%5)%2)//1)

'''Enter amount for withdrawal :64327
 100 notes =  643
 50 notes  =  0
 20 notes  =  1
 10 notes  =  0
 5 notes  =  1
 2 notes  =  1
 1 notes  =  0'''