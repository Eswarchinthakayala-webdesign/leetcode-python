class Solution(object):
    def lengthOfLastWord(self, s):
        list1=s.split()
     
        if not list1:
            return 0
        return len(list1[-1])
            
