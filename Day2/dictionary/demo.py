# mydict = {
#     101: "prashant",
#     102: "ashish",
#     "103": "mohini",
#     "104":"trivani",
#     101:"ashish",
#     104:"ashish"
# }
# print(mydict)

# a = mydict[102]  
# print(a)

# mydict[102]="peter" #to change old values
# print(mydict)

# for x in mydict:
#     print(x)  #used to print keys 

# for x in mydict.values():
#     print(x) #used to print values 

# for x , y in mydict.items():
#     print(x,y) # print both

# mydict["mobileno"] = 465746352  # add key and value pair
# print(mydict)

# mydict.pop(101) #pop() used for removing complete pair
# print(mydict)

# a ={(1,2):1,(2,3):2,(4,5):3} #tuple as a key
# print(a[4,5]) #3    here 4,5 is a key that is a tuple also in dictionary a

# a = { 'a':1 , 'b':2,'c':3}
# print(a['a','b']) # syntactical error key error , cannot have two key together 

# -----------------------------------------

# arr ={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# sum = 0 

# for i in arr:
#     sum += arr[i]
# print(sum) #4    

# -------------------------------------------

# dict = {}
# dict[1]=1
# dict['1']=2
# dict[1.0]=4

# print(dict)
# sum =0
# for k in dict:
#     sum+= dict[k]
# print(sum) 
   
# here on surface it looks like 7 will be the output, but the output is 6 since
# 1.0 is again considerd as 1 so it will update 1 , thus 2+4=6
# ---------------------------------------------

# my_dict ={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum = 0

# for k in my_dict:
#     sum+= my_dict[k]
# print(sum) #30
# print(my_dict) #{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}