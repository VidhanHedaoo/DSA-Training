#wap to count the no. of words in a string

string = input("Enter the sentence(string):")
count = 1

if string == "":
    count = 0
else:    
    for i in string:
        if i == " ":
           count+= 1

print(count)       