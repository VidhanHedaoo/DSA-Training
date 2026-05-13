#waf to count the frquency of element in a list using dictionatry

list = [1,2,2,3,4,3,5]
dict ={}

for i in list:
    if i not in dict:
       dict[i]=1
    else:
       dict[i]+=1 

print(dict) #{1: 1, 2: 2, 3: 2, 4: 1, 5: 1}
