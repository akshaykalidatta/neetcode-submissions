class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        top, right, bottom, left = 0, M, N, 0
        nums = set()
        ans = []
        while len(nums)!=N*M:
            #top
            for i in range(left, right):
                if (top,i) not in nums:
                    nums.add((top,i))
                    ans.append(matrix[top][i])

            #right
            for i in range(top, bottom):
                if (i,right-1) not in nums:
                    nums.add((i,right-1))
                    ans.append(matrix[i][right-1])

            #bottom
            for i in range(right-1, left-1, -1):
                if (bottom-1,i) not in nums:
                    nums.add((bottom-1,i))
                    ans.append(matrix[bottom-1][i])

            #left
            for i in range(bottom-1, top-1, -1):
                if (i,left) not in nums:
                    nums.add((i,left))
                    ans.append(matrix[i][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return ans
