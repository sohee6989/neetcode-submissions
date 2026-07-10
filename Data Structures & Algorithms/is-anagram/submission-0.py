class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

        for key, value in s_set.items():
            if value != 0:
                return False
        
        return True
            