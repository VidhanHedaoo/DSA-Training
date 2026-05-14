#input = prashant*is*a*good*programmer
#output = ****prashantisagoodprogrammer

# input = "prashant*is*a*good*programmer"
# # output = "****"
# newname = ""
# val =""
# for i in input:
#     if i != "*":
#     #    output += i
#      newname += i
#     else:
#         val += i

# # print(output)

# print(str(val+newname))

# ------------------------------------------------

#input = aaabbbbccceeeee
#output = a3b4c3e5

input = "aaabbbbccceeeee"

dict = {}

for i in input:
    if i not in dict:
     dict[i] = 1
    else :
       dict[i] += 1 

newstring = ""

for i,j in zip(dict,dict.values()):
   newstring += i
   newstring += str(j)
      
print(newstring) #a3b4c3e5

