class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        new_array = sorted(num_dict, key= num_dict.get, reverse = True)
        
        return new_array[:k]
            