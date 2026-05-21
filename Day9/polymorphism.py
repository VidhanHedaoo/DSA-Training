'''overloading -> constructor , method , operator'''
'''python only supports operator overloading'''

class Rbi:
    def __init__(self):
        print("Parent class constructor called.")

    def home_loan(self):
        print("Home Loan ROI = 8%")

    def education_loan(self):
        print("Education loan = 9%")


class Sbi(Rbi):

    def __init__(self):
        print("Child class constructor called.")
        super().__init__()

    def education_loan(self):
        print("Education loan = 10%")
        super().education_loan() # if we want to call parent method.


obj = Sbi()
# obj.education_loan()

# ---------------------------------------

