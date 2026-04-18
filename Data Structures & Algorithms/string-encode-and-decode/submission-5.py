# class Solution:

#     def getLength(self, str1: str) -> int:
#         res = 0
#         for i in str1:
#             res += 1

#         return res


#     def encode(self, strs: List[str]) -> str:
#         estr = ""
#         for s in strs:
#             length = self.getLength(s)
#             estr += f"{length}#{s}"

#         return estr


#     def decode(self, s: str) -> List[str]:
#         strs = []
#         i=0
#         start = 0
#         while i < len(s):
#             if s[i] != '#':
#                 i += 1
#             if s[i] == '#':
#                 length = int(s[start:i])
#                 strs.append(s[(i+1):length+i+1])
                
#                 i = length + i + 1
                
#         return strs
class Solution:

    def getLength(self, str1: str) -> int:
        res = 0
        for i in str1:
            res += 1

        return res


    def encode(self, strs: List[str]) -> str:
        estr = ""
        for s in strs:
            length = self.getLength(s)
            estr += f"{length}#{s}"

        return estr


    def decode(self, s: str) -> List[str]:
        strs = []
        length = ''
        i=0
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            if s[i] == '#':
                length = int(length)
                strs.append(s[(i+1):length+i+1])
                i = length + i + 1
                length = ''
                
        return strs

