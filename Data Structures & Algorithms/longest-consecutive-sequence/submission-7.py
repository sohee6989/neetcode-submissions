class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = {}
        nums.sort()
        prev_num = 0
        longest_num = 0
        max_longest_num = 0

        for num in nums:
            if num not in nums_hash and num == prev_num + 1:
                longest_num += 1
                nums_hash[num] = 1
            elif num in nums_hash:
                continue
            else:
                longest_num = 1
            prev_num = num
            max_longest_num = max(max_longest_num, longest_num)
        
        return max_longest_num



