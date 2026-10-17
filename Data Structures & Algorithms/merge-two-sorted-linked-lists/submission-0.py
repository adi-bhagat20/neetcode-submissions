# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        t1 = list1
        t2 = list2
        dummy = ListNode()
        temp = dummy
        while t1 and t2:
            if t1.val < t2.val:
                temp.next = t1
                t1 = t1.next
                temp = temp.next
            else:
                temp.next = t2
                t2 = t2.next
                temp = temp.next
        
        if t1:
            temp.next = t1
        
        if t2:
            temp.next = t2

        return dummy.next
            
