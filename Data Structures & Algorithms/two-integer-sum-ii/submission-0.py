class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        L = 0
        R = len(n) - 1

        while L <= R:
            if n[L] + n[R] == target:
                return [L+1 , R+1]
            
            if n[L]+n[R] > target:
                R-=1
            elif n[L]+n[R] < target:
                L+=1
        