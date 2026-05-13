#wap to count vowels and consonant
vowels = ['a','e','i','o','u']
name = "hello"
cons = 0
vow = 0

for i in name:
    if i in vowels:
        vow += 1
    else:
        cons += 1    

print(vow) #2
print(cons) #3