class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        count=0
        pointer_p=0
        pointer_n=0
        
        negative=[]
        positive=[]
        
        for i in nums:
            if i < 0:
                negative.append(i)
                
            else:
                positive.append(i)
                
        for i in nums:
            if count % 2 == 0:
                ans.append(positive[pointer_p])
                pointer_p +=1
                
            else:
                ans.append(negative[pointer_n])
                pointer_n +=1
                
            count +=1
            
            
        return ans