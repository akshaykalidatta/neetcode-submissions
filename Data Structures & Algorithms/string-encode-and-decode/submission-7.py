class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += str(len(i)) + '#' + i

        return enc
            
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i] != '#':
                length_str += s[i]
                i += 1
            length = int(length_str) 
            ans.append(s[i+1 : i+1+length])
            i = i + 1 + length
        return ans
