class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]

        max_height = 0
        for i in range(len(height)):
            max_height = max(max_height, height[i])

            left_max[i] = max_height
        
        max_height = 0
        for j in range(len(height)-1, -1, -1):
            max_height = max(max_height, height[j])
            right_max[j] = max_height

        for i in range(len(height)):
            max_area += min(left_max[i], right_max[i]) - height[i]

        return max_area