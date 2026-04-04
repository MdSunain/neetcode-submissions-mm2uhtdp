class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring = ''
        length = len(s1)

        for i in range(len(s2)-length+1):
            substring = s2[i:i+length]
            if sorted(substring) == sorted(s1):
                return True
        return False


