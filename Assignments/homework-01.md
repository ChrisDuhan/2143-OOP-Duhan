``` python
"""
Name: Chris Duhan
Email: chris.m.duhan@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 11:00 a.m.
"""

#A:

a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]
print()

#B:

x = [3, 1, 2, 1, 5, 1, 1, 7]
def remove_all(el,lst):
    for i in lst:
        lst.remove(el)
        
remove_all(1,x)
print(x)
print()

#C:

lst = [1, 2, 4, 2, 1]
def add_this_many(x, y, lst):
    for i in lst:
        if i == x:
        lst.append(y)
        
add_this_many(1, 5, lst)
print(lst)
print()

#D:

a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]
print()

#E:

x = [3, 2, 4, 5, 1]
def reverse(lst):
    for i in range(round(len(lst)/2)):
        #Using round to get an interger returned
        swap = lst[i]
        lst[i] = lst[len(lst)-(i + 1)]
        lst[len(lst)-(i + 1)] = swap
        
reverse(x)
print(x)
print()

#F:

def rotate(lst, k):
    #Using concatenation
    return lst[(k-1):] + lst[:(k-1)]
  
xrot = rotate(x, 3)
print(xrot)
print()

#H:

superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
superbowls['peyton manning'] = 1
superbowls['joe flacco'] = 1
print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'joe flacco': 1, ('eli manning', 'giants'): 2, 'joe montana': 4, 'tom brady': 3, 'peyton manning': 1}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', 'joe flacco': 1, ('eli manning', 'giants'): 5, 'joe montana': 4, 'tom brady': 3, 'peyton manning': 1}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
"""Prints: {3: 'cat', ('steelers', '49ers'): 11, 'peyton manning': 1, ('eli manning', 'giants'): 5,
'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}
"""
print()

#I:

d = {1:{2:3, 3:4}, 2:{4:4, 5:3}} 
def replace_all(d, x, y):
    for k in d.keys(): 
        if type(d[k]) == dict: 
            replace_all(d[k], x, y)
        elif d[k] == x: 
            d[k] = y
            
replace_all(d,3,1)
print(d)
print()

#J:

d = {1:2, 2:3, 3:2, 4:3}
def rm(d, x):
    #Using a list of keys to remove the key/value pairs
    delete = []
    for k in d.keys():
        if d[k] == x:
            delete.append(k)
    for k in delete:
        del d[k]
rm(d,2)
print(d)
```
