class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}

        for ch in s:
            if ch in s_hash:
                s_hash[ch] += 1
            else:
                s_hash[ch] = 1

        for ch in t:
            if ch in s_hash:
                s_hash[ch] -= 1

                if s_hash[ch] < 0:
                    return False
            else:
                return False
        
        for value in s_hash.values():
            if value != 0:
                return False

        return True