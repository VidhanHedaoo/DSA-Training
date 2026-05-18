#find the duplicate in list 

# list = [4,3,2,7,8,2,1,5,5]

# dict = {}
# result = []
# for i in list :
#     if i  in dict:
#         result.append(i)
#     else:
#         dict[i] = 1 

# print(result)      #[2, 5]

# ---------------------------------
#sort dictionary by key or value

input = {"C":3,"B":2,"A":1}
result ={}
for i in sorted(input):
    result[i] = input[i]

print(result) #{'A': 1, 'B': 2, 'C': 3}


