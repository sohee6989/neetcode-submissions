class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ''

        for ch in s:
            if ch.isalnum():
                sorted_s += ch.lower()
        
        l, r = 0, len(sorted_s) - 1

        while(l < r):
            if sorted_s[l] != sorted_s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
