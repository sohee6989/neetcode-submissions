class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums) -1

            while (l < r):
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    output_array = [nums[l], nums[i], nums[r]]
                    output_array.sort()
                    if output_array not in output:
                        output.append(output_array)
                    l += 1
                    r -= 1
        
        return output
        