# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ans = ListNode()
        curr = ans
        pointer = 1
        
        while list1:
            if (pointer < a + 1) or (pointer > b + 1):
                
                curr.next = ListNode(list1.val)
                list1 = list1.next
                curr = curr.next
                
            elif pointer == a + 1:
                list1 = list1.next
                while list2:
                    curr.next = ListNode(list2.val)
                    curr = curr.next
                    list2 = list2.next
                    
            else:
                list1 = list1.next
                    
            pointer += 1
            
        if pointer == a:
            while list2:
                curr.next = ListNode(list2.val)
                list2 = list2.next
                curr = curr.next
                
        return ans.next