class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        n = len(arr)
        for i in range(n - 1 , -1 , -1):
            original_val = arr[i]
            arr[i] = right_max
            right_max = max(original_val , right_max)
        
        return arr