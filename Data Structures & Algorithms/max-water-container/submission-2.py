class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                amount = (right - left) * heights[left]
                left += 1
            else:
                amount = (right - left) * heights[right]
                right -= 1
            
            max_amount = max(max_amount, amount)
        
        return max_amount
