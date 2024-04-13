class Solution(object):
    def convertToTitle(self, columnNumber):
        ans=[]
        while columnNumber:
            columnNumber,n=divmod(columnNumber-1,26)
            ans+=chr(n+ord('A'))
        return ''.join(reversed(ans))
