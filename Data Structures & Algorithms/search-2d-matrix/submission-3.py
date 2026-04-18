class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rlow, rhigh = 0, len(matrix)-1
        while rlow <= rhigh:
            rmid = (rlow+rhigh)//2
            if matrix[rmid][0] == target:
                return True
            if matrix[rmid][0] > target:
                rhigh = rmid - 1
            elif matrix[rmid][0] < target:
                clow, chigh = 0, len(matrix[0]) - 1
                while clow<=chigh:
                    cmid = (clow+chigh)//2
                    if matrix[rmid][cmid] == target:
                        return True
                    elif matrix[rmid][cmid] > target:
                        chigh = cmid - 1
                    else:
                        clow = cmid + 1
                rlow = rmid + 1

        return False 