"""
Valid Anagram
leetcode question link: https://leetcode.com/problems/valid-anagram/description/
"""
class ValidAnagram:
    def isAnagram(this, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCharMap = {}
        tCharMap = {}
        for i in range(len(s)):
            sCharMap[s[i]] = 1 + sCharMap.get(s[i], 0)
            tCharMap[t[i]] = 1 + tCharMap.get(t[i], 0)

        return sCharMap == tCharMap
    
    def isAnagramV2(this, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)