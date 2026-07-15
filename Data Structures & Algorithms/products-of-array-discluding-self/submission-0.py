class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        total_product = 1

        for num in nums:
            total_product *= num
        
        for i in range(len(nums)):
            if nums[i] == 0:
                product_without_zero = 1
                for j in range(len(nums)):
                    if i != j:
                        product_without_zero *= nums[j]
                output.append(product_without_zero)
            else:
                output.append(int(total_product / nums[i]))

        return output
