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
            res = False
            if curr.isWord:
                ans.append(words[curr.idx])
                curr.isWord = False
                
            if i<0 or j<0 or i>N-1 or j>M-1:
                return False

            if (i,j) in visited:
                return False

            if board[i][j] in curr.children:
                visited.add((i,j))
                res = dfs(i+1,j, curr.children[board[i][j]]) or dfs(i,j+1, curr.children[board[i][j]]) or dfs(i-1,j, curr.children[board[i][j]]) or dfs(i,j-1, curr.children[board[i][j]])
                visited.remove((i,j))

            return res
            
        for i in range(N):
            for j in range(M):
                if (i,j) not in visited:
                    _ = dfs(i, j, self.trie.root)

        return ans

    