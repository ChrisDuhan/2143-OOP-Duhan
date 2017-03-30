```python
"""
Chris Duhan
Manhattan Distance formula
"""

import math

class Cell(object):
    def __init__(self,row=None,col=None,color=None):
        self.occupied = False
        self.color = color
        self.location = [row,col]

    def __str__(self):
        return "[%s %s %s]" % (self.occupied,self.color,self.location)


def manhattan_distance(p1, p2):
    return abs(p2.location[0] - p1.location[0]) + abs(p2.location[1] - p1.location[1])

def cartesian_distance(p1, p2):
  return math.sqrt(pow((p2.location[0] - p1.location[0]), 2) + pow((p2.location[1] - p1.location[1]), 2)) 
  #math.sqrt() cuz it said sqrt was an undefined variable
  
cell1 = Cell(1,1)
cell2 = Cell(4,7)

print(manhattan_distance(cell1, cell2)) #9
print(cartesian_distance(cell1, cell2)) #6.708203932
```
