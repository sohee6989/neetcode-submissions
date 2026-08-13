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
                # 해시에 객체 자체를 저장해서 동일 유무를 비교!
                nums_hash[current] = [idx]
                current = current.next
                idx += 1
    
        return False
        

        