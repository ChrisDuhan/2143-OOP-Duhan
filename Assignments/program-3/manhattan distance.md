```python
class Cell(object):
    def __init__(self,row=None,col=None,color=None):
        self.occupied = False
        self.color = color
        self.location = [row,col]

    def __str__(self):
        return "[%s %s %s]" % (self.occupied,self.color,self.location)


def manhattan_distance(p1, p2):
    return abs(p2.location[0] - p1.location[0]) + abs(p2.location[1] - p1.location[1])

cell1 = Cell(1,1)
cell2 = Cell(4,7)

print(manhattan_distance(cell1, cell2))
```
