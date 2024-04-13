class Solution(object):
    def isPalindrome(self, s):
        s_f = "".join([char for char in lower(s) if char.isalnum()])
        return s_f == s_f[::-1]
        
        
