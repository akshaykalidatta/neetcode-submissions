class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort(key = lambda x: x[0], reverse=True)

        position, speed = [pair[0] for pair in pairs], [pair[1] for pair in pairs]
        
        stack = []
        for i, j in zip(position, speed):
            if len(stack) == 0:
                stack.append((target-i)/j)
            else:
                if (target-i)/j > stack[-1]:
                    stack.append((target-i)/j)

        return len(stack)