class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while(l < r):
            diff = r- l
            height = min(heights[r], heights[l])
            amount = diff * height
            max_amount = max(amount, max_amount)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return max_amount
