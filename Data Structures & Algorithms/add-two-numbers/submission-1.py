# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        t1 , t2 = l1 , l2
        ans = ListNode()
        ansptr = ans
        while t1 and t2:
            newNode = ListNode()
            if (t1.val + t2.val + carry) > 9:
                newNode.val = int((t1.val + t2.val + carry)%10)
                carry = 1
            else:
                newNode.val = t1.val + t2.val + carry
                carry = 0
            ansptr.next = newNode
            ansptr = ansptr.next
            t1 = t1.next
            t2 = t2.next

        while t1:
            newNode = ListNode()
            if (t1.val + carry) > 9:
                newNode.val = int((t1.val + carry)%10)
                carry = 1
            else:
                newNode.val = t1.val + carry
                carry = 0
            ansptr.next = newNode
            ansptr = ansptr.next
            t1 = t1.next

        while t2:
            newNode = ListNode()
            if (t2.val + carry) > 9:
                newNode.val = int((t2.val + carry)%10)
                carry = 1
            else:
                newNode.val = t2.val + carry
                carry = 0
            ansptr.next = newNode
            ansptr = ansptr.next
            t2 = t2.next

        if carry != 0:
            newNode = ListNode()
            newNode.val = carry
            ansptr.next = newNode
        return ans.next 








