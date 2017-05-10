```python
So the closest I came to useing code was looking up how to use certain things, the closest thing to being copied was the super init in the person-parent-child problem, if that counts I got it from stackoverflow.com.
```
## **Q1**
```python
def dirReduc(lst):
  reducableSteps = [("NORTH","SOUTH"),("SOUTH","NORTH"),("EAST","WEST"), ("WEST","EAST")]
  for i in range(len(lst)-1):
    for j in range(len(reducableSteps)):
      if lst[i],lst[i+1] == reducableSteps[j]:
        lst.pop(i)
        lst.pop(i)
"""
This is not working, I though I had a way to solve it but once you went back and clarified it made my way technicly ineffective.
While it still would have worked it didnt solve it in the way asked.
"""
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
    self.children = [child]
  
  def addChildren(self, newchild):
    self.children.append(newchild)
    
class Child(Person):
  def __init__(self, firstname, lastname, parent):
    super().__init__(firstname, lastname)
    self.parent = parent
```
## **Q7**
```python
from random import randint
class RoulettWheel(object):
    def __init__(self):
      self.wheel = {00:"green",0:"green",1:"red",2:"black",3:"red",4:"black",5:"red",6:"black",7:"red",8:"black",9:"red",10:"black",11:"black",12:"red",13:"black",14:"red",15:"black",16:"red",17:"black",18:"red",19:"red",20:"black",21:"red",22:"black",23:"red",24:"black",25:"red",26:"black",27:"red",28:"black",29:"black",30:"red",31:"black",32:"red",33:"black",34:"red",35:"black",36:"red"}

    def spin(self):
      num = self.wheel[randint(0,38)]
      if num == 37:
        num = 0
      elif num == 38:
        num = 00
      #return self.wheel[num]
      
      for k in self.wheel:
            if num in self.wheel[k]:
                res = {'Number':int(num), 'Color':str(k)}
                return res

class bet(object):
  def __init__(self, startamt, val, spot1, spot2):
    self.chips = startamt #how much is placed down
    self.payout = val #the payout multiplier if they win
    #spots 1 and 2 will be used to ensure the bet is in a valid location on the table, if spot 1 and 2 are the same the bet is on a single number, if they are different we'll check for the payout to see if it's a double or quardruple, if double we make sure the two numbers are adjacent, if quardruple we'll see if the numbers are caty-cornered. If the bet is not valid we can provide output to the user.

class Player(object):
  def __init__(self, name, buyin):
    self.name = name
    self.wallet = buyin
    """
    For now I see the game being played with a single player, but could be expanded by adding a player list to the game class.
    """
    pass
  
class RouletteTable(object):
  def __init__(self):
    """
    RouletteTable will provide a way to track how much is in a bet, and where it is placed.
    There are some numbers that while they are sequential in a numberline, they are not neighbors on the roulette table.
    For this reason the table might be best stored as a 2D array, so that any number can check its neighbors depending on what type of bet is placed.
    We would also have seperate spots for non-integer bets, (two-to-one, etc.) and special handeling for the zeros and who their neighbors are.
    RouletteTable will recieve the value from RouletteWheel once called and then check to see if: the number is one of the spots of their bet, if it fulfills a 1 to 18, 1 to 12, or similar bet, and make a payout if appropiete.
    """
    pass
  
class game(object):
  def __init__(self, player, buy_in):
    self.player = Player(player, buy_in)
    self.table = RouletteTable()
    self.wheel = RouletteWheel()
    """
    The game object will control the flow of players, if we choose to expand for more players, and even if not will check to see if the player wants to continue makong bets after each payout.
```
