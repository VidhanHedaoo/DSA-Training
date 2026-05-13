#wap to check if two strings are anagrams of each other
string1 = input("enter the string1: ")
string2 = input("enter the string2: ")
anagram = False
for i in string1:
    if i in string2:
       anagram = True

if anagram:
    print("Two Strings are anagram.")
else:
    print("Not a anagram.")    

