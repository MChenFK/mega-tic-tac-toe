from constants import *
from graphics import Line, Point

class Tile:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            fill_color = TILE_OUTLINE_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, fill_color)

        if self.has_right_wall:
            fill_color = TILE_OUTLINE_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, fill_color)
        
        if self.has_top_wall:
            fill_color = TILE_OUTLINE_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, fill_color)
        
        if self.has_bottom_wall:
            fill_color = TILE_OUTLINE_COLOR
        else:
            fill_color = BACKGROUND_COLOR
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, fill_color)