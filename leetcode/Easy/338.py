class Solution(object):
    def countBits(self, n):
        bits=[]
        counts=[]
        for i in range(n+1):
            bits.append(bin(i)[2:])
        for word in bits:
            counts.append(word.count("1"))
        return counts
