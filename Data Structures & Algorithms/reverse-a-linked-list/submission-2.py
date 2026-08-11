# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev 

            prev = current
            current = next_node

        # prev가 제일 앞 객체 하나를 가리키는 것
        return prev

# [3, 2, 1, 0] 연결리스트 뒤집기

# 초기 상태
# prev = None
# current = 3

# 3 → 2 → 1 → 0 → None


# [1회차]

# next_node = current.next
# → next_node = 2

# current.next = prev
# → 3 → None

# prev = current
# → prev = 3

# current = next_node
# → current = 2

# 현재 상태
# prev:    3 → None
# current: 2 → 1 → 0 → None


# [2회차]

# next_node = current.next
# → next_node = 1

# current.next = prev
# → 2 → 3 → None

# prev = current
# → prev = 2

# current = next_node
# → current = 1

# 현재 상태
# prev:    2 → 3 → None
# current: 1 → 0 → None


# [3회차]

# next_node = 0

# current.next = prev
# → 1 → 2 → 3 → None

# prev = 1
# current = 0


# [4회차]

# next_node = None

# current.next = prev
# → 0 → 1 → 2 → 3 → None

# prev = 0
# current = None


# while 종료

# return prev

# 결과:
# 0 → 1 → 2 → 3 → None