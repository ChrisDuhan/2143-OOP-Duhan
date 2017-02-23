import math

class rgbColor(Object):
  def __init__(self, r = None, g = None, b = None):
    if not r:
      r = 0
    if not g:
      g = 0
    if not b:
      b = 0
  
  def __str__(self):
    return ("red: ",self.r," green: ",self.g," blue: ",self.b)

  def __add__(self, color):
    return self.average(color)
    
  def average(self, color2):
    return (math.sqrt((pow(self.r,2)+pow(color2.r,2))/2),math.sqrt((pow(self.g,2)+pow(color2.g,2))/2),math.sqrt((pow(self.b,2)+pow(color2.b,2))/2))
