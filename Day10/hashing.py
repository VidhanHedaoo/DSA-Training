# hashing is a technique used to convert data into a fixed size value called hash value or hash code.
# constant time - O(1)

# hash function ? - it converts the input -> fixed index.

class Hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashfunction(self, key):
        return key % self.size
    
    def insert(self,key):
        index = self.hashfunction(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)

h = Hashtable(7)
h.insert(15)
h.insert(29)
h.insert(8)
h.insert(25)
h.insert(2)
h.display()
print("Hash address of 29 is ",h.hashfunction(29))

''' Output->
[[], [15, 29, 8], [2], [], [25], [], []]
Hash address of 29 is  1'''