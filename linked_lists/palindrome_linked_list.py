# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # O(n) O(1) time, space complexity
        # Base Case
        if head is None:
            return 
        
        fast = slow = head 
        while fast and fast.next : # Loop till at last or before last Node
                fast = fast.next.next # Move two steps ahead
                slow = slow.next # Move one step ahead

        prev = None # Pointer pointing prev
        current = slow

        while current:
            next_node = current.next 
            current.next = prev
            prev = current 
            current = next_node

        first = head
        second = prev
        while second:
                if first.val != second.val:
                    return False
                first = first.next
                second = second.next
        return True