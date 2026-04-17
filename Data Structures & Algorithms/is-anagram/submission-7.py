class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        sets = set(s)
        sett = set(t)

        for c in sets:
                maps[c] = s.count(c) 

        for c in sett:
            mapt[c] = t.count(c)

        return maps == mapt
        
           
