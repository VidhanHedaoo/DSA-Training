import csv
# f = open("employee.csv", 'a')
# a = csv.writer(f)
# # a.writerow(["EmpId","Name","Age"]) #ran only once to avoid coping the column name 

# empid = int(input("enter emp id : "))
# name  = input("enter employee name : ")
# age   = int(input("enter employee age : "))

# a.writerow([empid,name,age])
# print("File has created.")

q = open("student.csv", 'a')
b = csv.writer(q)
b.writerow(["stuId","stuName","phy","chem","math","Total","Percentage","Result"])

id = int(input("Enter id : "))
name = input("Enter name : ")
phy = int(input("Enter phy marks : "))
chem = int(input("enter chem marks : "))
math = int(input("enter maths marks : "))

total = phy + chem + math 
percentage = total/3
if percentage >= 40:
    result  = "pass"
else:
    result = "fail"    

b.writerow([id,name,phy,chem,math,total,percentage,result])    



