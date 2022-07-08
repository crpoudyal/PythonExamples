# Typecasting in python

a = "456"

print(type(a)) # <class 'str'>

a = int(a) # Typecast string to integer

# we cannot add sting with integer or vice versa

print(type(a)) # <class 'int'>

print(a + 4) # 460

a = float(a)

print(type(a)) # <class 'float'>

print(a - 3) # 453.0