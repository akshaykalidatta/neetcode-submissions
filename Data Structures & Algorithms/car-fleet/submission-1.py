class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = zip(position, speed)
        comb = sorted(comb, key=lambda x: x[0], reverse=True)
        stack = []
        for pos, sp in comb:
            if len(stack)==0 or stack[-1] < (target-pos)/sp:
                stack.append((target-pos)/sp)

        return len(stack)