class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = k
        l, r = 0, 0
        if k > 0:
            check = arr[l]
        res = 0

        while l <= len(arr) - k :
            if n - 1> 0:
                r += 1
                check += arr[r]

                n -= 1

            else:
                if check / k >= threshold:
                    res += 1
                check -= arr[l]
                l += 1
                r += 1
                if r < len(arr):
                    check += arr[r]

        return res