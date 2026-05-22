class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        wordList.append(beginWord)

        pattern_map = {}
        for i in wordList:
            for j in range(len(i)):
                pattern = i[:j] + '*' + i[j+1:]
                if pattern not in pattern_map:
                    pattern_map[pattern] = [i]
                else:
                    pattern_map[pattern].append(i)

        for p in pattern_map:
            words = pattern_map[p]
            for i in range(0, len(words)):
                for j in range(i+1, len(words)):
                    if words[i] not in adj:
                        adj[words[i]] = [words[j]]
                    else:
                        adj[words[i]].append(words[j])

                    if words[j] not in adj:
                        adj[words[j]] = [words[i]]
                    else:
                        adj[words[j]].append(words[i])

        ans = 0
        queue = deque()
        visited = set()
        if beginWord in adj:
            queue.append(beginWord) 
            visited.add(beginWord)
        else:
            return 0
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return ans + 1
                for j in adj[word]:
                    if j not in visited:
                        queue.append(j)
                        visited.add(j)

            ans+=1

        return 0
