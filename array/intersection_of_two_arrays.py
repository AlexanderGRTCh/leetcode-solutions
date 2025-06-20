class Solution(object):
    # O(n+m) time and space complexity
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        unique_set1 = set(nums1) # Initialize a set of Nums1's unique elements
        unique_nums2 = list(set(nums2)) # Init a List of Nums2 with only unique elements
        stack = []

        for i in unique_nums2:
            if i in unique_set1:
                stack.append(i)
        return stack