class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1

        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
       
        while True:
            half_len_index = start + (end - start) // 2

            if nums[start] == target:
                return start
            
            if nums[end] == target:
                return end

            if end - start == 1:
                return -1
         
            if nums[half_len_index] < target:
                start = half_len_index
            elif nums[half_len_index] > target:
                end = half_len_index
            else:
                return half_len_index

        return -1