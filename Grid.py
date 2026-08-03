import math
class PathData:
    def __init__(self, resistance: int, x1: int, y1: int, x2: int, y2: int):
        self.resistance = int(resistance)
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
    def get_color(self):
        if self.resistance <= 20:
            return "blue"
        elif self.resistance > 20  and self.resistance <= 27:
            return "orange"
        else: 
            return "red"
    # resistance on one line ~= 20 ohms
    def get_lines(self):
        line1 = Line(self.x1,self.y1,self.x2,self.y1)
        line2 = Line(self.x2,self.y1,self.x2,self.y2)
        return [line1, line2]
class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
