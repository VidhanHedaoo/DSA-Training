# class Name:
#     age = 30 #data member
#     def display(self): #method
#         print("hello bro") # self is a first default ...


# obj = Name() #object is a refrence variable
# print(obj.age)
# obj.display()       
# ------------------------------------------------------------
# class Student:
#     def __init__(self): #__init__ is a special method/variable # constructor
#         self.name = "prashant"
#         self.age = 30

#     def display(self):
#         print("Name =",self.name)
#         print("age =",self.age)
# stuobj = Student() #<__main__.Student object at 0x000001efe54a8830> 
# print(stuobj)
# ------------------------------------------------------------

# class Message:
#     def __init__(self): #constructor
#         print("I am constructor")

#     def shows(self):
#         print("class program")

# obj = Message()
# obj.shows()
# ------------------------------------------------------------

# Parameterized constructor
class StudentInfo:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def displayInfo(self):
        print("Name : ", self.name)
        print("age : ",self.age)
        print("Roll No : ",self.rollno)    

stuObj = StudentInfo("Trump",76,420) 
stuObj.displayInfo()
