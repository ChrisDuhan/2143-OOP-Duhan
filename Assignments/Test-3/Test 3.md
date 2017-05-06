## **Q1**
```python
def dirReduc(lst):
  reducableSteps = [("NORTH","SOUTH"),("SOUTH","NORTH"),("EAST","WEST"), ("WEST","EAST")]
  for i in range(len(lst)-1):
    for j in range(len(reducableSteps)):
      if lst[i],lst[i+1] == reducableSteps[j]:
        lst.pop(i)
        lst.pop(i)

dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"]
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) => []
```

## **Q3**
```python
from math import sqrt
from math import pow

class point(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "[%d,%d]" % (self.x, self.y)

class Shape(object):
  def __init(self,p1,p2):
      self.p1 = p1
      self.p2 = p2
  
  def area(self):
      pass
  
class Square(Shape):
  def __init__(self,p1):
    self.length = p1
  
  def perimeter(self):
    self.per = self.length * 4
    return self.per
    
  def area(self):
    self.squares_area = self.length * self.length
    return self.squares_area
  
class Rectangle(Shape):
  def __init__(self,p1,p2):
    self.h = p1
    self.w = p2
  
  def perimeter(self):
    self.per = (self.h + self.w) * 2
    return self.per
    
  def area(self):
    self.rec_area = self.h * self.w
    return self.rec_area

class Cube(Square):
  def __init__(self,p1):
    self.length = p1

  def surfaceArea(self):
    self.s_area = self.length * self.length * 6
    return self.s_area
  
  def volume(self):
    self.vol = self.length * self.length * self.length
    return self.vol
```
## **Q4**
```python
def counter(s):
  l = list(s)
  contains = []
  dups =[]
  for i in range(len(l)):
    if not l[i] in contains:
      contains.append(l[i])
    else:
      if not i in dups:
        dups.append(l[i])
  return dups


print(counter("aabbcde"))
```
## **Q5**
```python
def check(l):
  check_count = l[0]
  for i in range(len(l)):
    if check_count != l[i]:
      return None #null?
    else:
      check_count +=1
  return("Array is consecutive")
  
  
lst = [-4,-3,-1,0,1,2,3,4,5,6,7,8]
print(check(lst))
```

