class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        for i in range(n-1):
            max_arr = -1
            for j in range(i+1, n):
                max_arr = max(max_arr, arr[j])
            arr[i] = max_arr
        arr[n-1]=-1
        return arr
