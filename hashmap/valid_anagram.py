

class Solution(object):
    # Time O(n) space O(1) complexity
    # Simple hasmpah solution
    def isAnagram(self, s, t):
        # O(n+m) Time and O(1) Space complexity
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr_s = [0]*26 # Init array with 26 elements
        arr_t = [0]*26

        for c in s:
            arr_s[ord(c) - ord("a")] += 1 # Increment count for char c in arr_s
        
        for c in t:
            arr_t[ord(c) - ord("a")] += 1

        return arr_s == arr_t
            