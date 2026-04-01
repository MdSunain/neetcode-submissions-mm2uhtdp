class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        set_s = set(s)
        set_t = set(t)

        for i in set_s:
            s_map[i] = s.count(i)
        for i in set_t:
            t_map[i] = t.count(i)

        return s_map == t_map

