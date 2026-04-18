class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use dicts of sets. Prev approach takes 3* n^2 time. this sol takes 1 pass
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in sqrs[(i//3,j//3)]):
                        return False

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sqrs[(i//3,j//3)].add(board[i][j])

        return True
        