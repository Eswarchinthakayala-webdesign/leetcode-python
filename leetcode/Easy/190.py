class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1 
            temp =  n & 1 
            n >>=1
            result |= temp
        return result
