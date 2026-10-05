class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        numOfSubArr = 0
        windowArr = []
        for R in range(len(arr)):
            if R - L >= k:
                if sum(windowArr) / k >= threshold:
                    numOfSubArr += 1
                windowArr.remove(arr[L])
                L+=1

            windowArr.append(arr[R])
        if sum(windowArr) / k >= threshold:
            numOfSubArr += 1
        return numOfSubArr