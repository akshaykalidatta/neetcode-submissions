class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rlow = 0
        rhigh = len(matrix) - 1

        while rhigh >= rlow:
            rmid = rlow + ((rhigh-rlow)//2)
            if matrix[rmid][0] > target:
                rhigh = rmid - 1
            elif matrix[rmid][0] < target and matrix[rmid][len(matrix[0])-1] < target:
                rlow = rmid + 1
            # elif matrix[rmid][0] < target and matrix[rmid][len(matrix[0])-1] >= target:
            else:
                clow = 0
                chigh = len(matrix[0]) - 1

                while chigh >= clow:
                    cmid = clow + ((chigh-clow)//2)
                    if matrix[rmid][cmid] > target:
                        chigh = cmid - 1
                    elif matrix[rmid][cmid] < target:
                        clow = cmid + 1
                    else:
                        return True
                return False
        return False
