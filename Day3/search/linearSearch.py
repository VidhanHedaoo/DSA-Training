def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [1,2,3,4,8,7,9]

target = 7

result = linearSearch(array,target)

if result == -1:
    print("Target not found.")
else:
    print("Target found at index ",result)    