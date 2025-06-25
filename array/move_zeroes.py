class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time O(n) Space O(1) complexity
        # Base case 
        if not nums:
            return nums
        slow = fast = 0
        zero_count = 0
        for i in nums:
            if i == 0:
                fast += 1
                zero_count += 1
            if i != 0:
                nums[slow] = nums[fast] # Copy non-zero value to current slow index (that equals 0)
                slow += 1
                fast += 1
        for i in range(len(nums)-1, len(nums) - zero_count -1, -1): # Iterate from end zero_count times
            nums[i] = 0
        return nums

