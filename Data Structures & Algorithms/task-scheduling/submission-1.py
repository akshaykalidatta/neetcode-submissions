class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        freq = [0]*26
        for i in tasks:
            freq[ord(i)-ord('A')] += 1

        heap = []
        for i in range(len(freq)):
            if freq[i]>0:
                heapq.heappush(heap, ((-1)*freq[i], chr(i + ord('A'))))

        queue = deque()
        while True:
            if len(heap) == 0 and len(queue) == 0:
                break
            ans += 1
            while queue and queue[0][2] <= ans: 
                char, freq, time = queue.popleft()
                heapq.heappush(heap, ((-1)*freq, char))

            if len(heap) == 0:
                continue
            
            freq, char = heapq.heappop(heap)
            if (-1)*freq > 1:
                queue.append((char, (-1)*freq-1, ans+n+1))

            if queue and queue[0][2] <= ans:
                char, freq, time = queue.popleft()
                heapq.heappush(heap, ((-1)*freq, char))

        return ans