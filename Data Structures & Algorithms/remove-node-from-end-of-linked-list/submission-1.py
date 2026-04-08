# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        F = dummy
        S = dummy

        for _ in range(n+1):
            F = F.next

        while F:
            F = F.next
            S = S.next

        S.next = S.next.next
        
        return dummy.next
