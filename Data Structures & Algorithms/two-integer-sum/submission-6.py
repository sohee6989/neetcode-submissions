class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return sorted([i, nums_hash[target-nums[i]]])
            else:
                nums_hash[nums[i]] = i
        return [0]