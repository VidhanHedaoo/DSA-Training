# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()  

#-----------------------------------           

# n=int(input("Enter the number of rows : "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()   

# Output 
# Enter the number of rows : 5
# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E
# ------------------------------------

# n=int(input("Enter the number of rows : "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()  

# Output
# Enter the number of rows : 5
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# -------------------------------------

# n=int(input("Enter the number of rows : "))

# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+i),end=" ")
#     print()

# output
# A A A A A 
# B B B B 
# C C C 
# D D 
# E     

# ----------------------------------------

import time 
n=int(input("Enter the number of rows : "))

for i in range(1,n+1):
    print(" "*(n-i),end=" ") #multiply the space 
    for j in range(1,i+1):
        time.sleep(2)
        print("*",end=" ")
    print()