'''Recursion'''
# recursion uses stack memory , that's why try to avoid recursion 
# not memory/space efficient
# when we use recursion?
# when the main problem can be divided into similar sub problem then we use recursion.
# In iterartion we do not require stack memory 
# recursion is less time efficient because sys takes times to push pop the resursion function into the stack.

'''factorial Solution'''

# def fact(num):
#     if num <= 1 : # this is called base condition , recursion must execute towards base condition.
#         return 1
#     else:
#         return num*fact(num-1)   
# print(fact(5))   
 
#---------------------------------------------------------
 
'''capitalizeFirst solution using recursion'''

# def capitalize(arr):

#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:]) # arr[0][0].upper() = 'C' + arr[0][1:] = 'ar'  => 'Car'
#     return result + capitalize(arr[1:])

# arr = ['car','taco','banana']
# print(capitalize(arr)) #['Car', 'Taco', 'Banana']

# ------------------------------------------------------

'''Power fucntion using recursion'''

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(3,3)) # 27
# print(power(2,4)) # 16

# ------------------------------------------------------

'''product of array element'''

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:]) 

# arr = [1,2,3,4,5]
# print(productOfArray(arr)) #120

# -------------------------------------------------------

'''Reverse a string using recursion'''

# def reverse(string):
#     if len(string) <= 1:
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])

# print(reverse('Whatsapp')) #ppastahW

# ----------------------------------------------------

'''Recursive range'''

# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return str(num) + str(recursiveRange(num-1))

# print(recursiveRange(6)) #6543210

# ---------------------------------------------------

'''isPalindrome using recursion'''

# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome('awesome')) #False
# print(isPalindrome('abba')) #True

# -------------------------------------------------

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:],cb)
    return True

def isodd(num):
    if num %2 ==0:
        return False
    else:
        return True
    
print(someRecursive([1,2,3,4], isodd)) #True
print(someRecursive([14,6,8], isodd)) #False