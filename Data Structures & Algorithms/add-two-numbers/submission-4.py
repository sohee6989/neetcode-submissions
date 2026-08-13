# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        process = result
        next_val = 0
        is_over_under = False

        while l1 or l2:
            if not is_over_under:
                next_val = 0

            is_over_under = False
            if l1 and l2:
                cur_sum = l1.val + l2.val + next_val
            elif l1 and not l2:
                cur_sum = l1.val + next_val
            elif not l1 and l2:
                cur_sum = l2.val + next_val

            if cur_sum >= 10:
                value = cur_sum % 10
                next_val = cur_sum // 10
                is_over_under = True
                process.next = ListNode(value)
            else:
                process.next = ListNode(cur_sum)
            
            process = process.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        if is_over_under:
            process.next = ListNode(next_val)
        
        return result.next
        