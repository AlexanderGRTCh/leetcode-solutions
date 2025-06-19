class Solution(object):
    def containsDuplicate(self, nums):
        #O(n) time & space
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) # If nums length != with corresponding unique list
