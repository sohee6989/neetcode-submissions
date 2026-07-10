class Solution:
    def isPalindrome(self, s: str) -> bool:
        target_s = ''

        for ch in s.lower():
            if ch.isalnum():
                target_s += ch

        if target_s == '':
            return True
        
        for i in range(0, len(target_s) // 2 + 1):
            if target_s[i] != target_s[-i-1]:
                return False

        return True