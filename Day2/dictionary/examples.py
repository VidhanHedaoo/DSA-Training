# box= {}
# jars={}
# crates ={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(crates)
# print(len(crates[box])) #error 

# -------------------------------

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict): # we can use underscore instead of variable if that variable is a key in dictionary 
#     print(dict[_])  
# # 96
# # 98
# # 97
# --------------------------------

# rec = {"name" : "python","age":"20"}
# r = rec.copy() #it will not point to same address because we are not assigning it but copying it in a new variable
# print(id(r)==id(rec)) #false

# -------------------------------

# rec = {"name" : "python","age":"20"}
# id1 = id(rec)
# del rec

# rec = {"name" : "python","age":"20"}
# id2 = id(rec)
# print(id1==id2) #true #python will assign the new variable the exixting address if same value 

