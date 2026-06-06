class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final = []
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            else:
                final.append([i,j,k])

        flagx = flagy = flagz = 0

        for i, j, k in final:
            if i == target[0]:
                flagx = 1
            if j == target[1]:
                flagy = 1
            if k == target[2]:
                flagz = 1

        return True if flagx == 1 and flagy == 1 and flagz == 1 else False
