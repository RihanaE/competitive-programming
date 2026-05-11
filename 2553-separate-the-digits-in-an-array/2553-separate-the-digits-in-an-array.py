class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for i in nums:
            num = i
            temp = []
            while num != 0 :
                temp.append(num % 10)
                num = num // 10

            temp.reverse()
            answer.extend(temp)

        
        return answer