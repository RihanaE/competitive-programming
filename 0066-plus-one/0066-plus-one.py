class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1] + 1
        l=len(digits) - 1

        if digits[-1] < 10:
            return digits

        else:
            while digits[l] > 9:
                temp=digits[l]
                digits[l] =temp % 10
                l -=1

                if l <= -1:
                    digits.insert(0,temp // 10)
                else:
                    digits[l]= digits[l] + temp // 10

        return digits
