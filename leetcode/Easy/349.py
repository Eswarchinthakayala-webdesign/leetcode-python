class Solution(object):
    def intersection(self, nums1, nums2):
        num3=[]
        for num in nums1:
            if num in nums2:
                num3.append(num)
        num3=list(set(num3))
        return num3
            
