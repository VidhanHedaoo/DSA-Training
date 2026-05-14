#row wise max value
list = [[100,198,333,323],
        [122,232,221,111],
        [223,565,245,764]]

newlist = []
cmax = 0
for i in range(3):
    j=0
    max = list[i][j]
    for j in range(4):
        if list[i][j] > max:
            cmax = list[i][j] 

    newlist.append(cmax)        

print(newlist)  #[323, 221, 764]      