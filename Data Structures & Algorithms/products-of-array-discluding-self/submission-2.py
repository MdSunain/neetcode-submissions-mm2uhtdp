class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        pre_list = []

        for i in nums:
            pre_list.append(pre)
            pre*= i

        post = 1
        post_list = [0]*n

        for i in range(n-1,-1,-1):
            post_list[i] = post
            post *= nums[i]
        
        res= []
        for i in range(n):
            res.append(post_list[i]*pre_list[i])

        return res
