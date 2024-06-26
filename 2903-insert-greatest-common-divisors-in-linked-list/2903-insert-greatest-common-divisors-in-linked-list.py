# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcf(self, a, b):
        if(b == 0):
            return a
        else:
            return self.gcf(b, a % b)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        left, right = head, head.next
        while right:
            gcd = self.gcf(left.val, right.val)
            new_node = ListNode(gcd)
            left.next = new_node
            new_node.next = right
            left, right = right, right.next
            
        return head    