class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        # sort the freq
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        for num,count in freq.items():
            bucket[count].append(num)
        
        ans = []

        for i in range(n,0,-1):
            for ele in bucket[i]:
                ans.append(ele)
                if len(ans)==k:
                    return ans
