class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        for n in nums:

            if n in nums:
                leng = 1
                curr = n+1
                while curr in nums:
                    leng += 1
                    curr += 1
                maxi = max(maxi, leng)
        return maxi