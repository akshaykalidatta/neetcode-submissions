class Solution:
    def helper(self, i, j, m, n, board, currword, word, visited):
        if i >= m or j >= n or i < 0 or j < 0:
            return False

        if len(currword) > len(word):
            return False

        if not visited[i][j]:
            currword += board[i][j]
            if currword == word:
                return True
            visited[i][j] = True
            result = (self.helper(i+1, j, m, n, board, currword, word, visited) or
            self.helper(i-1, j, m, n, board, currword, word, visited) or
            self.helper(i, j+1, m, n, board, currword, word, visited) or
            self.helper(i, j-1, m, n, board, currword, word, visited))
            currword = currword[:-1]
            visited[i][j] = False

            return result
        

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        currword = ''
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helper(i, j, m, n, board, currword, word, visited):
                    return True

        return False

            