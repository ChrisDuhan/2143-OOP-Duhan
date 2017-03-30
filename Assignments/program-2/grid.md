```python
"""
Name: Chris Duhan
Email: chris.m.duhan@gmail.com
Assignment: Homework 2 - Grid
Due: March 28, 2017
"""

from graphics import *    # Zelle's simple OO graphics
import json

class Grid(object):
  def __init__(self):
    self.win  # The window we are drawing the grid in
    self.cell_width
    self.cell_height
    self.color_wheel = [  color_rgb(255,0,0), color_rgb(0,255,0), color_rgb(0,0,255),
                          color_rgb(255,255,0), color_rgb(255,0,255), color_rgb(0,255,255),
                          color_rgb(127,255,0), color_rgb(0,127,255), color_rgb(127,0,255),
                          color_rgb(255,127,0), color_rgb(0,255,127), color_rgb(255,0,127),
                          color_rgb(127,127,0), color_rgb(127,0,127), color_rgb(0,127,127),
                          color_rgb(255,255,127), color_rgb(255,127,255), color_rgb(127,255,255) ]
    self.cur_color = 0
    self.black = color_rgb(0,0,0)
    self.white = color_rgb(255,255,255)
    self.red = color_rgb(200,0,0)
    self.green = color_rgb(0,200,0)
    self.blue = color_rgb(0,0,200)
    self.grey = color_rgb(100,100,100)
    self.light_grey = color_rgb(200,200,200)
    self.nrows = 1
    self.n_sub_rows = 1
    self.n_sub_cols = 1
  
  def load(self, color_file):
    input = open(color_file, 'r')
    colors = json.loads(input.read())
    for i in colors:
      r = i['rgb'][0]
      g = i['rgb'][1]
      b = i['rgb'][2]
      self.color_wheel.append(color_rgb(r,g,b))
        
  def make(self, rows, cols, width, height):
    """Create the grid display, initially all white.
    rows, cols are the grid size in rows and columns.
    width, height are the window size in pixels.
    Args: 
        rows:  number of rows of cells in the grid (vertical divisions)
        cols:  number of columns of cells in the grid (horizontal divisions)
        width:  horizontal width of window in pixels
        height: vertical height of window in pixels
    Returns:  nothing
    """
    self.win = GraphWin("Grid", width, height)
    self.win.setCoords(0, 0, rows, cols)
    bkgrnd = Rectangle( Point(0,0), Point(width,height) )
    bkgrnd.setFill( color_rgb(255,255,255) ) # White background
    self.cell_width = width / cols
    self.cell_height = height / rows
    self.nrows = rows 

def get_cur_color(self):
    """Return the currently chosen color in the color wheel.  
    The color wheel is a list of colors selected to be contrast with each other. 
    The first few entries are bright primary colors; as we cycle through the color
    wheel, contrast becomes less, but colors should remain distinct to those with 
    normal color vision until the color wheel cycles all the way around in 18 
    choices and starts recycling previously used colors.   The color wheel starts
    out in position 0, so get_cur_color() may be called before get_next_color() has 
    been called. 
    
    Args:  none
    Returns:  
        a 'color' that can be passed to fill_cell
    """
    return self.color_wheel[self.cur_color]

def get_next_color(self):
    """Advance the color wheel, returning the next available color. 
    
    The color wheel is a list of colors selected to be contrast with each other. 
    The first few entries are bright primary colors; as we cycle through the color
    wheel, contrast becomes less, but colors should remain distinct to those with 
    normal color vision until the color wheel cycles all the way around in 18 
    choices and starts recycling previously used colors. 
    
    Args:  none
    Returns:  
        a 'color' that can be passed to fill_cell    
    """
    self.cur_color += 1
    if self.cur_color >= len(self.color_wheel) :
        self.cur_color = 0
    return self.color_wheel[self.cur_color]

def fill_cell(self, row, col, color):
    """Fill cell[row,col] with color.
    Args: 
        row:  which row the selected cell is in.  Row 0 is the top row, 
           row 1 is the next row down, etc.  Row should be between 0 
           and one less than the number of rows in the grid. 
        col:  which column the selected cell is in.  Column 0 is 
           the leftmost row, column 1 is the next row to the right, etc. 
           Col should be between 0 and one less than the number of columns
           in the grid. 
        color: What color to fill fill the selecte cell with.  Valid colors
           include grid.white, grid.black, and values returned by 
           grid.get_next_color() and grid.get_cur_color()
    """
    left = col
    right = col + 1
    top = self.nrows - (row + 1)
    bottom = self.nrows - row
    mark = Rectangle( Point(left,bottom), Point(right,top) )
    mark.setFill(color)
    mark.draw(self.win)
    
def label_cell(self, row, col, text, color=black):
    """Place text label on cell[row,col].
    Args: 
        row:  which row the selected cell is in.  Row 0 is the top row, 
           row 1 is the next row down, etc.  Row should be between 0 
           and one less than the number of rows in the grid. 
        col:  which column the selected cell is in.  Column 0 is 
           the leftmost row, column 1 is the next row to the right, etc. 
           Col should be between 0 and one less than the number of columns
           in the grid. 
        text: string (usually one character) to label the cell with
        color: Color of text label
    """

    xcenter = col + 0.5
    ycenter = self.nrows - (row + 1) + 0.5
    label = Text(Point(xcenter, ycenter), text)
    label.setFace("helvetica")
    label.setSize(20)  ## Is there a better way to choose text size? 
    label.setFill(color)
    label.draw(self.win)

def sub_grid_dim(self, rows, cols):
    """Divide each cell into rows x cols for sub-labeling
    Args:
       rows:  The number of rows of sub-cell in a cell.
       cols:  The number of columns of sub-cell in a cell.
    Returns: nothing
    Effects: Affects behavior of sub_label_cell
    """
    self.n_sub_rows = rows
    self.n_sub_cols = cols

def sub_label_cell(self, row, col, sub_row, sub_col, text, color=black):
      """Place label in subrow, subcol of row, col.
      Args:
        row:  Row of major grid (counting 0 as top row)
        col:  Column of major grid (counting 0 as leftmost column)
        sub_row:  Row in minor (interior) grid of cell
        sub_col:  Column in minor (interior) grid of cell
        text: Label (usually one character) to place there
        color: color of text
      """
      xcenter = col + ((self.sub_col + 0.5) / self.n_sub_cols)
      ycenter = self.nrows - (row + 1) + ((self.sub_row + 0.5) / self.n_sub_rows)
      # print("Placing subgrid label at ({},{})".format(xcenter,ycenter))
      label = Text( Point(xcenter, ycenter), text)
      label.setFace("helvetica")
      label.setSize(10)  ## Is there a better way to choose text size? 
      label.setFill(color)
      label.draw(self.win)
    

def close(self):
    """ Close the graphics window (shut down graphics). 
    Args: none
    Returns: nothing
    Effect:  the grid graphics window is closed. 
    """
    self.win.close()
  
if __name__ == "__main__":
    print("Testing grid: 3x3 with 3x3 subgrid")
    grid = Grid()
    grid.make(3,3,500,500)
    grid.sub_grid_dim(3,3)
    for row in range(3):
        for col in range(3):
            grid.fill_cell(row, col, white)
    grid.label_cell(0,0,"00")
    grid.label_cell(1,1,"11")
    grid.label_cell(2,2,"22")
    for i in range(3):
        for j in range(3):
             grid.sub_label_cell(0, 2, i, j, str(i)+str(j))

    input("Press enter to exit")
    grid.close()
    ```