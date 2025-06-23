# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # O(n) time O(1) space complexity
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case
        if not list1: return list2
        if not list2: return list1

        if list1.val >= list2.val:
            current = list2
            list2 = list2.next
        else:
            current = list1
            list1 = list1.next
        head = current
        while list1 and list2: # While both lists exist
            if list1.val <= list2.val:
                current.next = list1 # Current pointer point to list1 head node
                list1 = list1.next # Move list1 head to next node
            else:
                current.next = list2
                list2 = list2.next
            current = current.next #move current to next sorted node
        if list1 and not list2:
            current.next = list1
        else: current.next = list2
        return head
        