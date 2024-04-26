class Solution(object):
    def wordPattern(self, pattern, s):
        words=s.split()
        if len(pattern)!=len(words):
            return False
        p_to_word={}
        word_to_p={}
        for p,word in zip(pattern,words):
            if p not in p_to_word:
                if word in word_to_p:
                    return False
                p_to_word[p]=word
                word_to_p[word]=p
            elif p_to_word[p]!=word:
                return False
        return True
            
