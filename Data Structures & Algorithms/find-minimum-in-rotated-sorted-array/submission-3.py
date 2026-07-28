class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]

        while True:
            half_index = start + (end - start) // 2
            
            if end - start == 1:
                if nums[end] < nums[start]:
                    return nums[end]
                else:
                    return nums[start]
            else:
                if nums[start] > nums[half_index]:
                    end = half_index

                if nums[end] < nums[half_index]:
                    start = half_index
                
                if nums[start] < nums[half_index] and nums[half_index] < nums[end]:
                    return nums[start] 
        