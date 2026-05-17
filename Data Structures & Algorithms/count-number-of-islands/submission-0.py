class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or grid[i][j] == "0":
                return
            visited.add((i, j))
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans