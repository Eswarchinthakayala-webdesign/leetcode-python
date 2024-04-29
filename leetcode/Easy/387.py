class Solution(object):
    def firstUniqChar(self, s):
        for i in s:
            if s.rindex(i)==s.index(i):
                return s.index(i)
        return -1        
        
