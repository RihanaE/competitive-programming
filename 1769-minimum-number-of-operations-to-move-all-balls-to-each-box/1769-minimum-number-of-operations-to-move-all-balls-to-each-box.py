class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        length = len(boxes)
        output = []
        
        for j in range(length):
            no_one = 0
            for i in range(length):
                if boxes[i] == "1":
                    no_one += abs(j - i)
                    
            output.append(no_one)
        
        return output