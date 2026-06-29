class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.points:
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for x, y in self.points.keys():
            if x!=px and y!=py and abs(px-x) == abs(py-y):
                if (x, py) in self.points and (px, y) in self.points:
                    ans += self.points[(x, py)]*self.points[(px, y)]*self.points[(x,y)]

        return ans
        
