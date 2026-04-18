class Solution:

    def check(self, val: List[str]) -> bool:
        hashmap = set()
        for i in val:
            if i != '.':
                if i in hashmap:
                    return False
                hashmap.add(i)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if (self.check(row) == False):
                return False

        for i in range(len(board)):
            columns = [[] for _ in range(len(board))]
            for j in range(len(board[0])):
                columns[i].append(board[j][i])

            if (self.check(columns[i]) == False):
                return False


        for start in [0,3,6]:
            for end in [0,3,6]:
                cube = []
                for i in range(3):
                    for j in range(3):
                        cube.append(board[start+i][end+j])

                if(self.check(cube) == False):
                    return False

        return True
        