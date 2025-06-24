from collections import Counter

class Solution(object):
    # Time O(n) space O(1) complexity
    # Simple hasmpah solution
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        my_dict_s = Counter(s) # Init and populate dictionairy: Chars of s as keys, counts as values
        my_dict_t = Counter(t)
        
        return my_dict_s == my_dict_t 
                
