class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = {}
        output = []

        for num in nums:
            if num in nums_hash:
                nums_hash[num] += 1
            else:
                nums_hash[num] = 1
        
        sorted_nums_hash = dict(sorted(nums_hash.items(), key=lambda x: x[1], reverse = True))

        count = 0

        for key in sorted_nums_hash.keys():
            if count < k:
                output.append(key)
            else:
                break
            count += 1

        return output