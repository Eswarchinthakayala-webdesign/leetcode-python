class Solution(object):
    def plusOne(self, digits):
        carry=1
        for i  in range(len(digits)-1,-1,-1):
            sum=digits[i]+carry
            digits[i]=sum%10
            carry=sum//10

        if carry:
            return [1]+digits
        else:
            return digits         
            

        
