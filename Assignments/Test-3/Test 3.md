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
## **Q2**
```python
def makeChange(queue):
  bill25 = 0
  bill50 = 0
  if (queue[0] == 50) or (queue[0] == 100):
    return "NO"
  elif queue[1] == 100:
    return "NO"
  else:
    for i in range(len(queue)):
      if (queue[i] == 25):
        bill25 += 1
      elif (queue[i] == 50) and (bill25 >= 1):
        bill50 += 1
        bill25 -= 1
      elif (queue[i] == 100) and ((bill50 >= 1 and bill25 >= 1) or (bill25 >= 3)):
        if bill50 >= 1:
          bill50 -= 1
          bill25 -= 1
        else:
          bill25 -= 3
      else:
        return "NO"
  return "YES"
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
      return l[i]
    else:
      check_count +=1
  return None
```
## **Q6**
```python
class Person(object):
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def get_name(self):
    return '%s %s' % (self.firstname, self.lastname)
      
class Parent(Person):
  def __init__(self, firstname, lastname, child):
    super().__init__(firstname, lastname)
    self.firstname = firstname
    self.lastname = lastname
    self.children = [child]
  
  def addChildren(self, newchild):
    self.children.append(newchild)
    
class Child(Person):
  def __init__(self, firstname, lastname, parent):
    super().__init__(firstname, lastname)
    self.firstname = firstname
    self.lastname = lastname
    self.parent = parent
```
## **Q7**
```python
from random import randint
class RoulettWheel(object):
    def __init__(self):
      """
      Tell me what, why, where ...
      """
      self.wheel = {00:"green",0:"green",1:"red",2:"black",3:"red",4:"black",5:"red",6:"black",7:"red",8:"black",9:"red",10:"black",11:"black",12:"red",13:"black",14:"red",15:"black",16:"red",17:"black",18:"red",19:"red",20:"black",21:"red",22:"black",23:"red",24:"black",25:"red",26:"black",27:"red",28:"black",29:"black",30:"red",31:"black",32:"red",33:"black",34:"red",35:"black",36:"red"}

    def spin(self):
      num = self.wheel[randint(0,38)]
      if num == 37:
        num = 0
      elif num == 38:
        num = 00
      return self.wheel[num]

t = RoulettWheel()
print(t.spin())
```
