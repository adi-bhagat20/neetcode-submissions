# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        position_from_front = length - n 

        if position_from_front == 0:
            head = head.next
            return head
        t = head
        while position_from_front != 1:
            t = t.next
            position_from_front -= 1
        t.next = t.next.next
        return head
