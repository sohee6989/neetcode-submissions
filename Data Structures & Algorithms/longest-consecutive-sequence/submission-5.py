class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = list(set(nums))
        nums_hash.sort()
        
        l = 0
        longest_seq = 1 if len(nums) > 0 else 0
        max_longest_seq = longest_seq
                
        while l < len(nums_hash)-1: 
            if nums_hash[l] == nums_hash[l+1] - 1:
                longest_seq += 1
            else:
                longest_seq = 1
            l += 1
            max_longest_seq = max(max_longest_seq, longest_seq)

        return max_longest_seq