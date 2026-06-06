class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final = []
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            else:
                final.append([i,j,k])

        # if len(final)==1 and final[0]!=target: return False

        check = {}
        for i in target:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1

        for i, j, k in final:
            if i == target[0]:
                check[i] -= 1
            if j == target[1]:
                check[j] -= 1
            if k == target[2]:
                check[k] -= 1

        for x in check:
            if check[x] > 0:
                return False

        return True
