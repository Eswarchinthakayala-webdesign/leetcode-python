class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum=0
        for i in t:
            sum=sum+ord(i)
        for i in s:
            sum=sum-ord(i)
        return chr(sum)
