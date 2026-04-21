class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, (-1)*num)

        if len(self.large)!=0 and (-1)*self.small[0] > self.large[0]:
            element = (-1)*heapq.heappop(self.small)
            heapq.heappush(self.large, element)

        if len(self.large) > len(self.small) + 1:
            element = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1)*element)
        
        if len(self.small) > len(self.large) + 1:
            element = (-1)*heapq.heappop(self.small)
            heapq.heappush(self.large, element)

    def findMedian(self) -> float:
        #1. self.self.large > self.self.small - self.self.large[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        #2. self.self.small > self.self.large - self.self.small[0]
        if len(self.small) > len(self.large):
            return (-1)*self.small[0]

        #3. self.self.large == self.self.small - avg
        if len(self.small) == len(self.large):
            return (((-1)*self.small[0] + self.large[0]) / 2)
        