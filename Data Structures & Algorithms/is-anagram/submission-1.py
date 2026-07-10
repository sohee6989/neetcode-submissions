class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_set = {}

        for ch in s:
            if ch in s_set:
                s_set[ch] += 1
            else:
                s_set[ch] = 1
        
        for ch in t:
            if ch in s_set:
                s_set[ch] -= 1
            else:
                return False

        for value in s_set.values():
            if value != 0:
                return False
        
        return True
            