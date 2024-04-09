class Solution(object):
    def isPalindrome(self, x):
        temp=x
        sum=0
        if x<0:
            return False
        else:
            while temp>0:
                r=temp%10
                sum=sum*10+r
                temp=temp//10
            if x==sum:
                return True
            else:
                return False
            
