# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        store=[]
        current=head
        indx=0
        
        while current:
            store.append([indx,current.val])
            current=current.next
            indx +=1
            
        res=[0] * len(store)
        stack=[]
        l=0
        
        while l < len(store):
            if stack == []:
                stack.append(store[l])
                l +=1
                
            elif store[l][1] > stack[-1][1]:
                res[stack[-1][0]]=store[l][1]
                stack.pop()
            else:
                stack.append(store[l])
                l +=1
                
        return res