#what will be the output of the folllowing code

# init_taple = ()
# print(init_taple.__len__()) #0
# -----------------------------------------

# init_taple_a = 'a' , 'b'
# init_taple_b = ('a' , 'b')

# print(init_taple_a==init_taple_b) #true
# ------------------------------------------

# init_taple_a = '1' , '2'
# init_taple_b = ('3' , '4')

# print(init_taple_a+init_taple_b) #('1', '2', '3', '4')
# -------------------------------------------

# l = [1,2,3]
# init_tuple =('Python',) * (l.__len__() - l[::-1][0])
# print(init_tuple) #()
# --------------------------------------------

# init_tuple =('Python',) * 3 
# print(type(init_tuple)) #<class 'tuple'>   ('Python') = string and   ('Python',) = tuple

# --------------------------------------------

init_tuple = ((1,2),) * 7 # (1,2)(1,2)(1,2)(1,2)(1,2)(1,2)(1,2)
# print(len(init_tuple[3:8])) #4

