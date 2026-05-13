# s = "Python are High level programming Language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

'''Output
python are high level programming language
PYTHON ARE HIGH LEVEL PROGRAMMING LANGUAGE
pYTHON ARE hIGH LEVEL PROGRAMMING lANGUAGE
Python Are High Level Programming Language
Python are high level programming language
'''

#format function used for desired output format

name = "prashant"
sal = 5000
age = 28

print("{} sal is {} age is {}.".format(name,sal,age))
print("{0} sal is {1} age is {2}.".format(name,sal,age))
print("{x} sal is {y} age is {z}.".format(x=name,y=sal,z=age))
a = 1
print(f"{a} is a good boy")   #new python syntax

''' Output
prashant sal is 5000 age is 28.
prashant sal is 5000 age is 28.
prashant sal is 5000 age is 28.
1 is a good boy '''