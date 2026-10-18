# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = [] # stack of node
        seen = set()

        temp = head
        length = 0
        while temp:
            stack.append(temp)
            length += 1
            temp = temp.next
        t1 = head
        seen.add(t1)
        t2 = None
        count = 0
        while count != length:
            if count % 2 == 0:
                t2 = t1.next
                Next = stack.pop()
                if Next in seen:
                    t1.next = None
                    break
                seen.add(Next)
                t1.next = Next
                t1 = t1.next
            else:
                if t2 in seen:
                    t1.next = None
                    break
                t1.next = t2
                t1 = t1.next
                seen.add(t1)
            count+=1







