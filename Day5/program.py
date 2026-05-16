#wap to accept student name and marks from keyboard and create a dictionary
#also display student amrks by taking student name

# n= int(input("Enter the number of students: "))
# dict = {}
# for i in range(0,n):
#     name = input("Enter student name :")
#     marks = int(input("Enter marks        : "))
#     dict[name] = marks 

# while True:
#     name = input("Enter Student name to get marks :")
#     marks = dict.get(name,-1)

#     if marks == -1:
#         print("Student not found")
#     else:
#         print("The marks of ",name," is ",marks) 

#     option = input("Do you want to find another student(y/n):")

#     if option=="n":
#         break
#------------------------------------------------------------------------
# 
'''wap to access each character of string in forwrd and backward direction by using while loop'''

# input = "Learning python is very easy" 
# i = 0

# while i < len(input) :
#     print(input[i],end="")
#     i += 1
# print("")

# i = len(input)-1
# while i >= 0  :
#     print(input[i],end="")  
#     i -= 1

# --------------------------------------------------------------------

# str1 , str2 = input("Enter the strings(encrypted and decrypted) : ").split()
# #input = asdfg asdfgh
# for i in str2:
#     if i not in str1:
#         print(i) # output-> h

# --------------------------------------------------------------------
'''Find vowels in string''' 
# v = ['a','e','i','o','u']
# word = input("Enter the word to be search for vowel:").lower()

# found = []

# for i in word:
#     if i in v:
#         if i not in found:
#             found.append(i)
            
# print(found)            

# ------------------------------------------------------------------

x , y , z= map(int,input().split())
mylist =[]

for i in range(x):
    a = int(input("Enter distance: "))
    mylist.append(a)

for i in mylist:
    if i >= y and  i <=z :
        print(i,end=" ")
        
''' 6 30 50 #input
    Enter distance: 29
    Enter distance: 38
    Enter distance: 12
    Enter distance: 48
    Enter distance: 39
    Enter distance: 55
3   8 48 39 '''



