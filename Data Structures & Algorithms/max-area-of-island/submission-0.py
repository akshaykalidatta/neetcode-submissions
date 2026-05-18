class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        visited = set()

        def dfs(i, j):
            if i<0 or j<0 or i>=ROWS or j>=COLS or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            length = 1 + dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
            return length

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    length = dfs(i, j)
                    ans = max(length, ans)

        return ans
