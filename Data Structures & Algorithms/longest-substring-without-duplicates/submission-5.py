class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        left, right = 0, 1
        used = set()

        if s:
            used.add(s[left])

        while right < len(s):
            while s[right] in used:
                used.remove(s[left])
                left += 1
            used.add(s[right])
            right += 1
            longest_substring = max(longest_substring, len(used))
            

        return max(longest_substring, len(used))
        