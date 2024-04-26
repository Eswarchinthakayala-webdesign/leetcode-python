class Solution(object):
    def moveZeroes(self, nums):
        ptr=0
        for num in nums:
            if num!=0:
                nums[ptr]=num
                ptr+=1

        for i in range(ptr,len(nums)):
            nums[i]=0
        return nums   
