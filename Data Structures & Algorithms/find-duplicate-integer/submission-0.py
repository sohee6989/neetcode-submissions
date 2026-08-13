class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_hash = {}

        for num in nums:
            if num in nums_hash:
                return num
            else:
                nums_hash[num] = 1
        