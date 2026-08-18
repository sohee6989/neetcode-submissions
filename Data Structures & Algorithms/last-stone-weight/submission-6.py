class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            first_large_num = stones.pop()
            second_large_num = stones.pop()

            if first_large_num > second_large_num:
                new_num = first_large_num - second_large_num
                stones.append(new_num)
        
        if stones:
            return stones[0]
        else:
            return 0