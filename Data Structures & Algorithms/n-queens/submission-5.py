class Solution:
    def helper(self, r, col, posDiag, negDiag, currBoard):
        if r == self.n:
            self.ans.append(currBoard.copy())
            return

        for i in range(self.n):
            if i not in col and (r+i) not in posDiag and (r-i) not in negDiag:
                currBoard[r] = '.'*i + 'Q' + '.'*(self.n-i-1)
                col.add(i)
                posDiag.add(r+i)
                negDiag.add(r-i)
                self.helper(r+1, col, posDiag, negDiag, currBoard)
                col.remove(i)
                posDiag.remove(r+i)
                negDiag.remove(r-i)
                currBoard[r] = '.'*self.n

        

    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        self.ans = [] 
        self.n = n

        currBoard = ['.'*n for i in range(n)]

        self.helper(0, col, posDiag, negDiag, currBoard)

        return self.ans