class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(0, len(nums) - k + 1):
            array = nums[i:i+k]
            output.append(max(array))

        return output