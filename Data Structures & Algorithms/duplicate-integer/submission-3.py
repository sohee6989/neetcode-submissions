class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = {}

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set[num] = 1
        
        return False
