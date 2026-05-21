
'''Static variable '''
# class Student:
#     @staticmethod
#     def get_personalDetails(firstname,lastname):
#         print("your personal details = ",firstname," ",lastname)

#     def get_contactDetails(mobile_no,roll_no):
#         print("your Contact details = ",mobile_no," ",roll_no)
    
# Student.get_personalDetails("Prashant","jha")
# Student.get_contactDetails(123456455,1234)    

# -------------------------------------------------

'''Inheritance''' 
# class College:
#     def collegename(self):
#         print("Modern College")

# class Student(College):
#     def studentInfo(self):
#         print("Name : Prashant Jha")
#         print("Branch : Mca") 
              
# obj = Student()
# obj.collegename()
# obj.studentInfo() 

# -------------------------------------------------

'''MultiLevel Inheritance'''

# class College:
#     def collegename(self):
#         print("Modern College")

# class Student(College):
#     def studentInfo(self):
#         print("Name : Prashant Jha")
#         print("Branch : Mca") 
              
# class Exam(Student):
#     def subject(self):
#         print("subject1: Math")
#         print("subject2: Stat")
#         print("subject1: DBMS")              


# obj = Exam()
# obj.collegename()
# obj.studentInfo() 
# obj.subject()

# -------------------------------------------------

'''Multiple Inheritance'''

class SubMarks:   # class-1
    math = int(input("Enter paper marks of math : "))
    DE = int(input("Enter paper marks of design engineering : "))
    c = int(input("Enter paper marks of c language : "))
    english = int(input("Enter paper marks of english : "))


class PractMarks:   # class-2
    cpract = int(input("Enter practical marks of c language : "))


class Result(SubMarks, PractMarks):   # child class
    def total(self):
        if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 20:
            print("pass")
        else:
            print("fail")


obj = Result()
obj.total()
