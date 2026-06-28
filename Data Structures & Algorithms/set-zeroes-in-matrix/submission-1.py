class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N, M =len(matrix),len(matrix[0])
        row, col = set(), set()

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(N):
            for j in range(M):
                if i in row or j in col:
                    matrix[i][j] = 0

        