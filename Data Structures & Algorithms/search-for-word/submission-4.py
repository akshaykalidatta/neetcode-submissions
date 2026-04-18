class Solution:
    def helper(self, i, j, idx):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or idx >= len(self.word):
            return False

        if self.visited[i][j]:
            return False

        if self.word[idx] != self.board[i][j]:
            return False

        if idx == len(self.word)-1:
            return True

        self.visited[i][j] = True
        res = (self.helper(i+1, j, idx+1) or
                self.helper(i-1, j, idx+1) or
                self.helper(i, j+1, idx+1) or
                self.helper(i, j-1, idx+1)
                )
        self.visited[i][j] = False
        return res       

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.board = board
        self.word = word
        self.visited = [[False for i in range(self.n)] for j in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                if self.helper(i, j, 0):
                    return True

        return False