class Solution(object):
    def isAnagram(self, s, t):
        t="".join(sorted(t))
        s="".join(sorted(s))
        if s==t:
            return True
        else:
            return False
            
