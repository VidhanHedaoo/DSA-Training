
input1 = "ababacbab" 
input2 = "ab"
count = 0
for i in range(len(input1)):
    # print(input1[i]+input1[i+1])
    if i+1 < len(input1) and input1[i]+input1[i+1] == input2:
          count += 1
            
print(count)
    