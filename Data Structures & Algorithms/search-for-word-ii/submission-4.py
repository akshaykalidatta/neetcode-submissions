class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, i):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        curr.idx = i

class Solution:
    def buildTrie(self, words):
        self.trie = Trie()
        for i in range(len(words)):
            self.trie.insert(words[i],i)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        N, M = len(board), len(board[0])
        self.buildTrie(words)
        ans = []
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()


        def dfs(i, j, curr):
            if curr.isWord:
                ans.append(words[curr.idx])
                curr.isWord = False

            if i < 0 or j < 0 or i >= N or j >= M:
                return
            if (i, j) in visited:
                return

            c = board[i][j]
            if c in curr.children:
                visited.add((i, j))
                child = curr.children[c] 
                dfs(i + 1, j, child)
                dfs(i, j + 1, child)
                dfs(i - 1, j, child)
                dfs(i, j - 1, child)
                visited.remove((i, j))

                if not child.children and not child.isWord:
                    del curr.children[c]
            
        for i in range(N):
            for j in range(M):
                if (i,j) not in visited:
                    _ = dfs(i, j, self.trie.root)

        return ans

    