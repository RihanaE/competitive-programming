class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        ans = num

        for i in range(len(n)):
            if n[i] == "6":
                ans = int(n[:i] + "9" +n[i + 1:])
                break

        return ans