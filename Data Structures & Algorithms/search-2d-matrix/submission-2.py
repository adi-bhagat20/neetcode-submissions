class Solution:
    def bs(self , arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix) , len(matrix[0])

        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid = top + (bot - top)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                # found the row in which element is
                return self.bs(matrix[mid], target)
        return False


