class new:
    b = 30
    def __init__(self):
        self.a = 10
        self.name = "prashant"

obj1 = new()
obj2 = new()
obj3 = new()
obj1.a = 20 #instance variable acessed by instance name
new.b = 50 # static variable updated via  class name 
 
print(obj1.a)
print(obj2.a)
print(obj3.a)
obj1.b = 40  # static variable updated for only that obj ie obj1 b = 40
print(obj1.b)
print(obj2.b) # here obj2 still have b = 50
print(obj3.b) # same here