class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        visited = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        heapq.heappush(heap, (grid[0][0], (0,0)))
        while heap:
            wt, (x, y) = heapq.heappop(heap)
            ans = max(ans, wt)
            if (x, y) in visited: continue
            
            if x==ROWS-1 and y==COLS-1: return ans
            visited.add((x,y))
            
            for dr,dc in directions:
                if (x+dr)<0 or (y+dc)<0 or (x+dr)>=ROWS or (y+dc)>=COLS:
                    continue
                if (x+dr, y+dc) not in visited:
                    heapq.heappush(heap, (grid[x+dr][y+dc], (x+dr, y+dc)))
                    

        