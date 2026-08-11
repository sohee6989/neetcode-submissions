class Solution:
    def isPalindrome(self, s: str) -> bool:
        mid = 0
        new_s = ''

        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        
        if len(new_s) == 0 or len(new_s) == 1:
            return True

        if len(new_s) % 2 == 0:
            mid = int(len(new_s) / 2)
        else:
            mid = int(len(new_s) // 2 - 1)
        
        for i in range(mid + 1):
            if new_s[i] != new_s[-i-1]:
                return False

        return True