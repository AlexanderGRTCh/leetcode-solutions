class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Time: O(n) Space: O(1)
        res = [1] * len(nums) # Initiate array with 1s
        prefix = suffix = 1 
        
        # Compute prefix products
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Compute suffix products and multiply with res[i]
        for i in reversed(range(len(nums))):
            res[i] *= suffix # Mulitple with products of elements after i
            suffix *= nums[i] # Compute suffix with new element nums[i]

        return res


        