# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nums_hash = {}

        current = head
        idx = 0
        while current:
            if current in nums_hash:
                return True
            else:
                nums_hash[current] = [idx]
                current = current.next
                idx += 1
    
        return False
        

        