# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode()
        current = merge_list
        
        while list1 or list2:
            # print("1", list1.val)
            # print("2", list2.val)
            # print("merge", merge_list.val)
            if not list1:
                current.next = list2
                break
            
            if not list2:
                current.next = list1
                break

            if list1.val > list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next
        
        return merge_list.next