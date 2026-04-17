class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for c in s:
                maps[c] = s.count(c) 

        for c in t:
            mapt[c] = t.count(c)

        return maps == mapt
        
           
