class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        sorted_s1 = sorted(s1)

        while r - 1 < len(s2):
            sub_str = s2[l:r]

            if sorted_s1 == sorted(sub_str):
                return True
            l += 1
            r += 1

        return False 