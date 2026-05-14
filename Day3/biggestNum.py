def findbiggestNumber(samplearr):
    biggestNo = samplearr[0]

    for i in range(1,len(samplearr)):
        if samplearr[i] > biggestNo:
            biggestNo = samplearr[i]
    print(biggestNo)

arr = [5,7,9,2,3,4]
findbiggestNumber(arr)

#Time complexity
# def findbiggestNumber(samplearr):     -> value is not assigned , only the address of arr 
#     biggestNo = samplearr[0]          -> O(1)

#     for i in range(1,len(samplearr)): -> O(N)
#         if samplearr[i] > biggestNo:  -> O(1)
#             biggestNo = samplearr[i]  -> O(1)
#     print(biggestNo)                  -> O(1)

# arr = [5,7,9,2,3,4]                   -> O(1)
# findbiggestNumber(arr)                -> O(1)

# Final time complexity = O(1) + O(1) + O(1) + O(1) + O(N) = O(N)