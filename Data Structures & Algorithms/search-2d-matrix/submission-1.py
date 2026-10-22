class Solution:
    def bs(self , arr , low , high , target):
        if low > high:
            return False
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            return self.bs(arr, low ,mid - 1, target)
        else:
            return self.bs(arr , mid + 1 , high , target)

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
                low = 0
                high = COLS - 1
                return self.bs(matrix[mid] , low , high , target)
        return False


