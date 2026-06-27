class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N, M = len(matrix), len(matrix[0])
        for i in range(N):
            for j in range(M):
                if i<=j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            for j in range(M//2):
                matrix[i][j], matrix[i][M-j-1] = matrix[i][M-j-1], matrix[i][j]

