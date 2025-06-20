class Solution(object):
    # O(n) Time and Space complexity
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if not stack: # If stack isEmpty return false
                    return False
                top = stack.pop()
                if ord(i) - ord(top) > 2: # 0 < Ascii difference between close-open parenthesis <= 2
                    return False
                elif ((ord(i) - ord(top) == 1 and ord(i) != 41)
                or (ord(i) - ord(top) == 2 and (ord(i) != 93 and ord(i) != 125))):
                    return False
        return len(stack) == 0 # Valid if stack isEmpty 
                
