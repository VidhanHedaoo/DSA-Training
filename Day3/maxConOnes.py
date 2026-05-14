#find the maximum number of consecutive 1s in a binary array
list = [1,1,0,1,1,1,0,1,1,1,1]
maxCon = 0
for i in list:
    if i == 1:
        maxCon += 1
    else:
        maxCon = 0    

print(maxCon)  #4

