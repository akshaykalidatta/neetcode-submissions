class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque()
        visited = set()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        length = 0
        while queue and fresh>0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)>=ROWS or (c+dc)>=COLS or grid[r+dr][c+dc]==0 or grid[r+dr][c+dc]==2:
                        continue
                    if (r+dr,c+dc) not in visited:
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
                        fresh -= 1

            length += 1

        return length if fresh == 0 else -1