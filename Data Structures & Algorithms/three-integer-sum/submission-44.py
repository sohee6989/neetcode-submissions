class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        output_hash = {}

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                answer = []

                if three_sum > 0:
                    r -= 1
                elif three_sum == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                else:
                    l += 1

                if answer and (answer[0][0], answer[0][1], answer[0][2]) not in output_hash:
                    output.append(answer[0])
                    output_hash[(answer[0][0], answer[0][1], answer[0][2])] = 1

        return output

