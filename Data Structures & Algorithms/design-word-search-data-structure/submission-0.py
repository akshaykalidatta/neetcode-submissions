class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def helper(self, word, i, curr) -> bool:
        if i == len(word):
            return curr.isWord

        if word[i] == '.':
            for c in curr.children:
                if self.helper(word, i+1, curr.children[c]):
                    return True

        if word[i] in curr.children:
            if self.helper(word,i+1,curr.children[word[i]]):
                return True
            
        return False

    def search(self, word: str) -> bool:
        curr = self.root
        return self.helper(word, 0, curr)
        
