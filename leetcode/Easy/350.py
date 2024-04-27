class Solution(object):
    def intersect(self, nums1, nums2):
        freq={}
        for num in nums1:
            freq[num]=freq.get(num,0)+1
        intersection=[]
        for num in nums2:
            if num in freq and freq[num]>0:
                intersection.append(num)

                freq[num]-=1
        return intersection
            
