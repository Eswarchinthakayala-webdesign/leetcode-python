class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_code=bin(n)[2:]
        count=0
        for i in binary_code:
            if i=='1':
                count+=1
        return count
            
