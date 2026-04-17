class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_arr = -1
        for j in range(len(arr)-1,-1,-1):
            new_max = max(max_arr, arr[j])
            arr[j] = max_arr
            max_arr = new_max
        return arr
