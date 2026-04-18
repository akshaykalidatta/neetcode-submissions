class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ('0' <= ch <= '9') or ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                clean += ch.lower()

        i, j = 0, len(clean)-1

        while j>i:
            if clean[i] != clean[j]:
                return False

            i+=1
            j-=1

        return True