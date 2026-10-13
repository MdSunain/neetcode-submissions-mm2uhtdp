class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        present = {}
        for i in range(len(nums)):
            if target-nums[i] in present:
                return [present[target-nums[i]],i]
            present[nums[i]] = i
        return [-1,-1]
