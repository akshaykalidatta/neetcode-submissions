class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq,aq = deque(), deque()
        pv, av = set(), set()
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                    pq.append((i, j))
                    pv.add((i, j))
                if i == ROWS-1 or j == COLS-1:
                    atlantic.add((i, j))
                    aq.append((i, j))
                    av.add((i, j))

        #pacific dfs
        while pq:
            for i in range(len(pq)):
                r, c = pq.popleft()
                pv.add((r, c))
                for dr, dc in directions:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)>=ROWS or (c+dc)>=COLS:
                        continue
                    if heights[r+dr][c+dc] < heights[r][c]:
                        continue
                    if (r+dr, c+dc) not in pv:
                        pq.append((r+dr, c+dc))
                        pacific.add((r+dr, c+dc))
                        pv.add((r+dr, c+dc))

        #atlantic dfs
        while aq:
            for i in range(len(aq)):
                r, c = aq.popleft()
                av.add((r, c))
                for dr, dc in directions:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)>=ROWS or (c+dc)>=COLS:
                        continue
                    if heights[r+dr][c+dc] < heights[r][c]:
                        continue
                    if (r+dr, c+dc) not in av:
                        aq.append((r+dr, c+dc))
                        atlantic.add((r+dr, c+dc))
                        av.add((r+dr, c+dc))

        ans = []
        for (i, j) in pacific:
            if (i, j) in atlantic:
                ans.append([i, j])

        return ans