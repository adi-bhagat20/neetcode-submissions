# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        
        t1 = None
        t2 = head

        while t2 and t2.next:
            t2 = head.next
            head.next = t1
            t1 = head
            head = t2
        head.next = t1
        return head