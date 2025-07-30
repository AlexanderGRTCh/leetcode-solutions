class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity O(n) Space O(n)

        hashNums = {}   # 3,3 Target 6
        index = 0
        for i in nums:
            # If Target - value exist in hashmap
            if (target - i) in hashNums:
                return (hashNums[target-i], index)
            hashNums[i] = index
            index += 1

        
