# import re

# count = 0
# pattern = re.compile("function")

# matcher = pattern.finditer("A function in pyhton is defined by def a statement. The geenral syntax looks like this: def function-name(Parameter list):"\
#                            " statements, i.e. the function body. The parameter python list consists of none or more parameters.")

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(),"...",i.group())
# print("The number of occurences : ",count)
''' Output->
2 ... 10 ... function
92 ... 100 ... function
144 ... 152 ... function
The number of occurences :  3
'''

# -------------------------------------------------------------

# import re

# count = 0

# matcher = re.finditer("def","A function in pyhton is defined by def a statement. The genaral syntax looks like this: def function-name(Parameter list):"\
#                            " statements, i.e. the function body. The parameter python list consists of none or more parameters.")

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(),"...",i.group())
# print("The number of occurences : ",count)

''' Output->
24 ... 27 ... def
35 ... 38 ... def
88 ... 91 ... def
The number of occurences :  3
'''
# ------------------------------------------------------------

# import re
# count = 0

# obj = input("Enter any one character to be searched : ")
# matcher = re.finditer(obj,"A function in pyhton is defined by def a statement. The genaral syntax looks like this: def function-name(Parameter list):"\
#                       " statements, i.e. the function body. The parameter python list consists of none or more parameters.")

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(),"...",i.group())
# print("The number of occurences : ",count)   

''' Output ->
Enter any one character to be searched : y
15 ... 16 ... y
33 ... 34 ... y
65 ... 66 ... y
156 ... 157 ... y
174 ... 175 ... y
The number of occurences :  5
'''
# ----------------------------------------------------------------

# match() is used to find the string at the begining/starting  of the pararaph 
# import re
# count = 0

# obj = input("Enter a string to be searched : ")
# mtch = re.match(obj,"A function in pyhton is defined by def a statement. The genaral syntax looks like this: def function-name(Parameter list):"\
#                       " statements, i.e. the function body. The parameter python list consists of none or more parameters.")

# print(mtch)

# if mtch != None:
#     print("match Found at begining level.")
#     print(mtch.start(), " ... ",mtch.end())
# else:
#     print("There is no matching at the begining level.")    

''' Output->
Enter a string to be searched : A
<re.Match object; span=(0, 1), match='A'>
match Found at begining level.
0  ...  1


Enter a string to be searched : function
None
There is no matching at the begining level.'''

# ----------------------------------------------------------------------
# fullmatch() return none if not fully matched else return obj

# import re
# count = 0

# obj = input("Enter a string to perform match operation : ")
# mtch = re.fullmatch(obj,"python is very.")

# print(mtch)

# if mtch != None:
#     print("match found")
#     print(mtch.start(), " ... ",mtch.end())
# else:
#     print("Not found.") 

''' Output->
Enter a string to perform match operation : python is very.
<re.Match object; span=(0, 15), match='python is very.'>
match found
0  ...  15   
'''   
# ------------------------------------------------------------------
# to check wheater the given mail : is valid gmail id or not?

# import re
# obj = input("Enter your mail id : ")

# m = re.fullmatch("\\w[a-zA-z0-9_.]*@gmail[.]com",obj)
# if m != None:
#     print("Valid E-mail Id.")
# else:
#     print("Invalid E-mail Id entered.")    

# ------------------------------------------------------------------

# import re
# obj = input("Enter your phone no. : ")

# m = re.fullmatch("[0-9]\\d{9}",obj)
# if m != None:
#     print("Valid phone no..")
# else:
#     print("Invalid phone no. entered.")    

# -------------------------------------------------------------------

# import re
# count = 0

# obj = input("Enter a string to perform search operation : ")
# mtch = re.search(obj,"python is very important language.")

# print(mtch)

# if mtch != None:
#     print("match found")
#     print(mtch.start(), " ... ",mtch.end())
# else:
#     print("Not found.")

''' Output->
Enter a string to perform search operation : very
<re.Match object; span=(10, 14), match='very'>
match found
10  ...  14
'''
# ---------------------------------------------------------

# import re
# count = 0

# mtch = re.findall('[0-9]',"23456tyghq2q324546uhgfd345t")
# mtch2 = re.findall('[A-Z]',"DRCFHB4e5r6t7y8HId456&*idsUYT")
# mtch3 = re.findall('[a-z]',"SRFVBNJhgfde456tyhJI(*&6ew#$%TYU*)")

# print(mtch)
# print(mtch2)
# print(mtch3)

''' Output->
['2', '3', '4', '5', '6', '2', '3', '2', '4', '5', '4', '6', '3', '4', '5']
['D', 'R', 'C', 'F', 'H', 'B', 'H', 'I', 'U', 'Y', 'T']
['h', 'g', 'f', 'd', 'e', 't', 'y', 'h', 'e', 'w']
'''

# --------------------------------------------------------

# import re
# mtch = re.sub('[a-zA-Z]','*',"2345 ABCD habc derr") # aadhar example
# print(mtch)

''' output ->
2345 **** **** ****
'''
# --------------------------------------------------------

# import re
# mtch = re.subn('[0-7]','@',"sd3434sd65f7gddf") 
# print(mtch)
# print("the string is = " ,mtch[0])
# print("the number of replacment is = ", mtch[1])

''' Output->
2345 **** **** ****
('sd@@@@sd@@f@gddf', 7)
the string is =  sd@@@@sd@@f@gddf
the number of replacment is =  7
'''
# ---------------------------------------------------------

# import re
# f1 = open("input.txt","r")
# for i in f1:
#     mtch = re.findall('[0-9]',i)

# if mtch != None:
#     print("Found string")
#     print(mtch)
# else:
#     print("Not found.")

''' Output->
Found string
['1', '2', '3', '4', '5', '6', '7', '9', '8', '7', '5', '6', '8', '0', '9', '6', '5', '6', '5', '3', '5', '5', '0', '9', '8', '7'] 
'''  



