import math

noOfPlot = int(input("Enter the no. of plot: "))
plots = input("Enter plots(space separated): ")

list  = []

for i in plots.split():
    root = math.sqrt(int(i))
    if root == int(root):
        list.append(int(i))

print("Total eligible plots = ",len(list))        

#output  
'''Enter the no. of plot: 8
Enter plots(space separated): 79 77 54 81 48 34 25 16 
Total eligible plots =  3 '''   
      







