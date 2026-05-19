class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque()
            visited = set()
            queue.append((i, j))
            visited.add((i, j))
            length = 1
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        if (r+dr)<0 or (c+dc)<0 or (r+dr)>=ROWS or (c+dc)>=COLS or grid[r+dr][c+dc] == -1:
                            continue

                        if  (r+dr, c+dc) not in visited:
                            queue.append((r+dr, c+dc))
                            visited.add((r+dr, c+dc))
                            grid[r+dr][c+dc] = min(length, grid[r+dr][c+dc])

                length += 1

            return

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j)
        