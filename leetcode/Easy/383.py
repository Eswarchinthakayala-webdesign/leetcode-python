class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote)>len(magazine):
            return False
        count=0
        ransomNote_counter=set()
        for char in ransomNote:
            if char not in ransomNote_counter:
                ransomNote_counter.add(char)
                if ransomNote.count(char)>magazine.count(char):
                    return False
        return True      
