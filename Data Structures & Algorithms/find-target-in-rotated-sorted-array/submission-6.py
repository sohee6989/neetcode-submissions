class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start + end) // 2
            print("start", start)
            print("end", end)

            if nums[start] == target:
                return start
            
            if nums[end] == target:
                return end
            
            if nums[mid] == target:
                return mid
            
            if start == mid or end == mid:
                break
            
            if nums[start] < target and nums[mid] >= target:
                end = mid
            elif nums[start] > nums[mid] and nums[start] < target:
                end = mid
            elif nums[start] > nums[mid] and nums[mid] > target:
                end =  mid
            else:
                start = mid
        
        return -1
        