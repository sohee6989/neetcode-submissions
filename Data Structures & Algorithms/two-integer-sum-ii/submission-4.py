class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in nums_hash:
                return [nums_hash[diff], i + 1]
            else:
                nums_hash[numbers[i]] = i + 1
        