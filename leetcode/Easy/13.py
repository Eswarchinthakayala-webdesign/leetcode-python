class Solution(object):
    def romanToInt(self, s):
        romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
        result=0
        i=0
        while i<len(s):
            if i<len(s)-1 and romans[s[i]]<romans[s[i+1]]:
                result+=romans[s[i+1]]-romans[s[i]]
                i+=2
                
            else:
                result+=romans[s[i]]
                i+=1
        return result
            
