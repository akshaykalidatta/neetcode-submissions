class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        temp = set("".join(words))
        for i in temp:
            adj[i] = []

        def firstDiff(s1, s2):
            minlen = min(len(s1), len(s2))
            if len(s1)>len(s2) and s1[:minlen]==s2[:minlen]:
                return -1
            if s1==s2:
                return 0
            
            i, j = 0, 0
            while i<len(s1) and j<len(s2):
                if s1[i]!=s2[j]:
                    return (s1[i],s2[j])
                else:
                    i+=1
                    j+=1
            return 0

        for i in range(1, len(words)):
            res = firstDiff(words[i-1], words[i])
            if res == -1:
                return ""
            if res == 0:
                continue
            src, dst = res
            adj[src].append(dst)

        ans = []
        visited = set()
        path = set()
        def dfs(node):
            if node in visited: 
                return True
            if node in path:
                return False
            path.add(node)
            for j in adj[node]:
                if not dfs(j):
                    return False
            path.remove(node)
            visited.add(node)
            ans.append(node)
            return True


        for i in adj:
            if not dfs(i):
                return ""

        return ''.join(ans[::-1])