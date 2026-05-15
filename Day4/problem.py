data  = input("Enter Data and key: ") #input = 12312312 3 
dict = {}
digit = data[-1]

for i in data:
    if i == " ":
        break 
    else:
        if i not in dict:
           dict[i] = 1
        else:
          dict[i] += 1

print(dict[digit]) 

'''
Output
5723782333 3
4
'''





