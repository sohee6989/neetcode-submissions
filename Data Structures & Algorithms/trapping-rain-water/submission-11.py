class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        left_max_height = height[0]
        
        for l in range(len(height)):
            left_max_height = max(left_max_height, height[l])
            left_max[l] = left_max_height
        
        right_max = [0 for _ in range(len(height))]
        right_max_height = height[len(height)-1]
        for r in range(len(height)-1, -1, -1):
            right_max_height = max(right_max_height, height[r])
            right_max[r] = right_max_height

        result = 0

        for i in range(len(height)):
            min_val = min(left_max[i], right_max[i])
            result += (min_val - height[i])

        return result