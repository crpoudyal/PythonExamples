# input() function take input from the user

name = input("Enter your name")

print("Welcome "+name+" to python code")

# All the data taken through input() function are String

a = input("Enter any Number")

print(type(a)) # <class 'str'>

a = int(a) # Convert a to an Integer (if possible)

print(type(a)) # <class 'int'>