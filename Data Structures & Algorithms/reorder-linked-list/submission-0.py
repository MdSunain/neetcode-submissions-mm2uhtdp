class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find middle (slow/fast pointer)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split & reverse second half
        second = slow.next
        slow.next = None  # Split
        
        prev = None
        while second:
            next_temp = second.next
            second.next = prev
            prev = second
            second = next_temp
        
        # 3. Merge alternately (in-place)
        first, second = head, prev
        while second:
            # Save nexts
            f_next, s_next = first.next, second.next
            
            # Interleave
            first.next = second
            second.next = f_next
            
            # Move forward
            first = f_next
            second = s_next