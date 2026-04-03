class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        output = []
        for i in range(0,n-2):
            j, k = i+1, n-1
            while j<k:
                target = nums[i]+nums[j]+nums[k]
                if target==0 and [nums[i],nums[j],nums[k]] not in output:
                    output.append([nums[i],nums[j],nums[k]])
                
                elif target<0:
                    j+=1
                else:
                    k-=1
        return output