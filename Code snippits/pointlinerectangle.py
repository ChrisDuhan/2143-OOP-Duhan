import math

class point(object):
  def __init__(self, x, y):
    self.coordinates = (x, y)
    if not (x, y):
      self.coordinates = (0, 0)
  
  def move_point(self, dx, dy):
    return ((self.coordinates[0] - dx), (self.coordinates[1] - dy))
    
class line(object):
  def __init__(self, point1, point2):
    line_start = point1
    line_end = point2
    
  def line_length(self):
    return math.sqrt(pow(abs(self.line_start[0] - self.line_end[0]), 2) + pow(abs(self.line_start[1] - self.line_end[1]), 2))
    
class rectangle(object):
  def __init__(self, point1, point2):
    upper_right = point1
    lower_left = point2
    
  def area(self):
    return abs(self.upper_right[0] - self.lower_left[0]) * abs(self.upper_right[1] - self.lower_left[1])
    
  def perimeter(self):
    return (abs(self.upper_right[0] - self.lower_left[0]) + abs(self.upper_right[1] - self.lower_left[1])) * 2
