class Solution(object):
    def singleNumber(self, nums):
        flag=0
        for i in nums:
            flag=flag^i
        return flag
            
