class Solution(object):
    def searchInsert(self, nums, target):
       
        if target not in nums:
         nums.append(target)
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            
