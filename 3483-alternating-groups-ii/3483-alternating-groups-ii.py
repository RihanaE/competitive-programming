class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left = 0
        right = 0
        res = 0
        length = len(colors)

        while left < len(colors):
            if right - left + 1 == k:
                print(right, left)

                res += 1
                left += 1

            if colors[(right + 1) % length] == colors[right % length]:
               
                left = right + 1
                
            right += 1

        return res