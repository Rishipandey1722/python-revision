# 1) Name, objects and mutability
# Everything is object . variables are name pointing towards objects.
# == checks equality and  is check indentity



#mutability matters...

# a = [1 , 2]
# b = a
# a.append(3)
# b.append(4)
# print(a)
# print( a is b)

# functions

def bad(x, bucket = []): # bad function
    bucket.append(x)
    return bucket

def good(x, bucket = None): # good function 
    if bucket is None:
        bucket = []
    
    bucket.append(x)
    return bucket
