class Solution:
    def helper(self, i, candidates, target, currcomb, ans, check):
        if check < 0:
            return
        if check == 0:
            ans.append(currcomb.copy())
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j]==candidates[j-1]:
                continue
            currcomb.append(candidates[j])
            self.helper(j+1, candidates, target, currcomb, ans, check - candidates[j])
            currcomb.pop()
        

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, currcomb = [], []
        self.helper(0, candidates, target, currcomb, ans, target)
        return ans
        