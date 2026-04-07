# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid
        mid = 0
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # divided the lists
        second = slow.next
        slow.next = None
        
# reverse l2
        
        p = None
        while second:
            n = second.next
            second.next = p
            p = second
            second = n

# merge
        first, second = head, p
        while second:
            fn, sn = first.next, second.next

            first.next = second
            second.next = fn

            first = fn
            second = sn



        
