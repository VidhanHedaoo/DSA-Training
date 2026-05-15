salary = int(input("Enter your salary :"))
rating = float(input("Enter your performance apraisal rating:"))
increament = 0
if rating >= 1 and rating <=3:
    increament += salary * 10/100
elif rating >= 3.1 and rating <=4:
    increament += salary * 40/100
elif rating >= 4.1 and rating <=5:
    increament += salary * 50/100
else:
    print("Invalid rating")

print("Incremented salary = ",increament+salary)

# ----------------------------------------------------

'''basicSal = 20000
we have to calculate the 
houserent of basicSal = 20%
ta of basicSal = 30%
da of basicSal = 45%
calculate grossSalary '''

# basicSal = 20000

# hra = basicSal*20/100
# ta = basicSal*30/100
# da = basicSal*45/100

# grossSal = basicSal + hra + ta + da
# print("Gross Salary = ",grossSal)

# ------------------------------------------------------

