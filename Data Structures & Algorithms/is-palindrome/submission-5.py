class Solution:
    def isPalindrome(self, s: str) -> bool:
        array_s = s.strip().lower()
        target_s = ''

        for i in range(len(array_s)):
            if array_s[i].isalnum():
                target_s += array_s[i]

        if target_s == '':
            return True
        
        for i in range(0, len(target_s) // 2 + 1):
            if target_s[i] != target_s[-i-1]:
                return False

        return True