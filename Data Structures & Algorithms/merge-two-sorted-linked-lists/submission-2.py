# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode() 
        current = merge_list
        # merge_list로 돌리면 처음 시작 위치를 잃게 된다.
        # merge_list = 시작점 고정
        # current = 현재 연결할 위치, 계속 이동
        
        while list1 or list2:
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