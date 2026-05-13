#check the palindrome:
#wap to check if a given string is a palindrome 

string = input("enter the string: ")
rev = ""
for i in range(len(string)-1,-1,-1):
     rev += string[i]

if rev==string :
    print("It is a palindrome")
else:
    print("not a palindrome")  

#also can be solved as 
# if name = name[::-1]
#     print("palindrome")
# else
#     print("not a palindrome")           