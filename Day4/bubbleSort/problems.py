# def bubbleSort(array):
#     for i in range(len(array)-1):

#         for j in range(len(array)-1-i):
#             if array[j] > array[j+1]: 
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#     return array            

            
# array =[64,34,25,12,22,11,90]
# print(bubbleSort(array))
# ------------------------------------------

#question Find the repeated no. in an interger (security key problem)
# 

num = [5,7,8,3,7,8,9,2,3]
dict= {}

for i in num:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

count = 0
for i in dict.values():
    if i > 1:
        count += 1

print(count," digit are repeated.") 

# another method but not as efficient as above code.
# num = [5,7,8,3,7,8,9,2,3]
# newlist=[]

# for i in range(len(num)):
#     count =0
#     key = num[i]
#     j =i+1

#     while j< len(num):
#         if key ==num[j]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))            
      