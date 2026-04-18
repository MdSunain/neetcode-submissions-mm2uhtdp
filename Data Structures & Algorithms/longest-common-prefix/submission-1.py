class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       cp = ''
       for i in range(len(strs[0])):
        curr = strs[0][i]
        for s in strs:
            if i == len(s) or curr != s[i]:
                return cp
        cp += curr
       return cp