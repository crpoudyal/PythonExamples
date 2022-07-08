# String concatinating

from this import d


greeting = "Hello, "

name = "Rj Poudyal"

print(greeting + name) 

# Accessing String data with index

data = "Nepal"
'''
N-- 0
e-- 1
p-- 2
a-- 3
l-- 4
'''
print(data[0]) # N
print(data[1]) # e
print(data[2]) # p
print(data[3]) # a
print(data[4]) # l

# Accessing string from 0 index upto 2 index 

print(data[0:2]) #  Ne
print(data[:2]) # same as data[0:2]
print(data[2:5]) # including 2 up to 4
print(data[2:]) # same as data[2:5]

# Accessing strings data using negative index

print(data[-5]) # N
print(data[-4]) # e
print(data[-1]) # l

# Slicing with skip value
data = "PythonProgramming"
print(data[0::2]) # ptopormig

print(data[0:5:3]) # ph -- including upto 4 skiping 2 character