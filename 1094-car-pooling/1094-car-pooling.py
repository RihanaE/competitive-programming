class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda k: k[1])
        stack=[]
        
        for no,fro,to in trips:
            stack.append((fro,no))
            stack.append((to,-no))
        
        stack.sort()
        num=0
        l=0
        
        while l < len(stack):
            num +=stack[l][1]
            if num > capacity:
                return False
            
            l +=1
            
        return True
    