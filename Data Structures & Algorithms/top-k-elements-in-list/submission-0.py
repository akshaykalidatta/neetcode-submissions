class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap,ans = {}, []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sort = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        i =0
        for key, value in sort:
            ans.append(key)
            i += 1
            if i == k:
                break

        return ans
