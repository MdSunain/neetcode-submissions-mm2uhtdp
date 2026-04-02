class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxi = 0
        for n in nums:

            if n-1 not in numset:
                leng = 0
                while (n+leng) in nums:
                    leng += 1
                maxi = max(maxi, leng)
        return maxi