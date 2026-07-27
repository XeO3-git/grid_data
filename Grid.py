class PathData:
    def __init__(self, resistance: int, x1: int, y1: int, x2: int, y2: int):
        self.resistance = int(resistance)
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
        # self.minDist = self.__get_min_dist(); # use this to figure out which nodes to go through
    # def __gen_min_dist():
    def get_color(self):
        if self.resistance <= 20:
            return "blue"
        elif self.resistance > 20  and self.resistance <= 27:
            return "orange"
        else: 
            return "red"
    # resistance on one line ~= 20 ohms
