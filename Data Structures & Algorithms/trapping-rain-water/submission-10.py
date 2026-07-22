class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [ 0 for i in range(len(height))]
        r_max = [ 0 for i in range(len(height))]
        max_height = 0
        max_area = 0;

        for i in range(len(height)):
            max_height = max(max_height, height[i])
            l_max[i] = max_height
        max_height = 0
        for i in range(len(height)-1, -1, -1):
            max_height = max(max_height, height[i])
            r_max[i] = max_height

        for i in range(len(height)):
            cur_height = min(l_max[i], r_max[i])
            if cur_height - height[i] > 0:
                max_area += (cur_height - height[i])
        
        return max_area