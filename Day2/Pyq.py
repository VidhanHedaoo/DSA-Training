#to count symbols and numbers in a message 
# string = input("Enter the message:")
# count=0

# for chr in string:
#     z = ord(chr)
#     if z >= 65 and z<=90 :
#         continue
#     elif z>=97 and z<=122  :
#         continue   
#     else:
#         count+=1

# print(count)     

# -----------------------------------------------

#product of array except self
#given an array, return an array where each element is the product of all the element in the array except itself

arr = [1,2,3,4]
new = []

for i in arr:
    product=1
    for j in arr:
        if j==i: continue
        else:
         product *= j
    new.append(product)

print(new)   #[24, 12, 8, 6]         