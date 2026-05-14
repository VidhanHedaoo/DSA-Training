# Removing spaces from the string:
# 1. rstrip() -> to remove spaces at right hand side
# 2. lstrip() -> to remove spaces at left hand side
# 3. strip() -> to remove spaces from both side

city = input("Enter your city name: ")
scity = city.strip()

if scity == "Hyderabad":
    print("Hello Hyderabad")
elif scity == "Chennai":
    print("Hello madrasi.")
elif scity == "Banglore":
    print("Hello kannadiga.")
else:
    print("your entered city is invalid.")    