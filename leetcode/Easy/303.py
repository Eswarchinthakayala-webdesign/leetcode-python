class NumArray(object):

    def __init__(self, nums):
        self.pre_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.pre_sum[i+1]=self.pre_sum[i]+nums[i]
        

    def sumRange(self, left, right):
        return self.pre_sum[right+1]-self.pre_sum[left]


