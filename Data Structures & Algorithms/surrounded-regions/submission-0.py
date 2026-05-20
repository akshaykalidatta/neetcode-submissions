class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        queue = deque()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or j == 0 or i == ROWS-1 or j == COLS-1) and board[i][j]=='O':
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if (r+dr)<0 or (c+dc)<0 or (r+dr)>=ROWS or (c+dc)>=COLS or board[r+dr][c+dc] == 'X':
                        continue
                    if (r+dr, c+dc) not in visited:
                        queue.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited:
                    board[i][j] = 'X'

