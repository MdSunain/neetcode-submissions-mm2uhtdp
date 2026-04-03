class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        l = 0
        r = len(heights)-1

        while(l<r):
            h = min( heights[l],heights[r])
            b = r-l
            output = max(output, h*b)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return output