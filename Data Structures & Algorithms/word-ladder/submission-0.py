class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        def wordDiff(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff+=1
                if diff>1:
                    return False
            return True

        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        for i in range(0, len(wordList)):
            for j in range(i, len(wordList)):
                if i!=j and wordDiff(wordList[i], wordList[j]):
                    if wordList[i] not in adj:
                        adj[wordList[i]] = [wordList[j]]
                    else:
                        adj[wordList[i]].append(wordList[j])

                    if wordList[j] not in adj:
                        adj[wordList[j]] = [wordList[i]]
                    else:
                        adj[wordList[j]].append(wordList[i])

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
