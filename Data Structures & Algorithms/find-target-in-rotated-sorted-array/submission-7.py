class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start + end) // 2

            if nums[start] == target:
                return start
            
            if nums[end] == target:
                return end
            
            if nums[mid] == target:
                return mid
            
            if start == mid or end == mid:
                break
            
            # start -> mid 오름차순
            if nums[start] < target and nums[mid] >= target:
                end = mid
            # start > mid 인 상황에서, start보다 큰 값인 target
            elif nums[start] > nums[mid] and nums[start] < target:
                end = mid
            # start > mid 인 상황에서, mid보다 작은 값인 target
            elif nums[start] > nums[mid] and nums[mid] > target:
                end =  mid
            else:
                start = mid
        
        return -1
        