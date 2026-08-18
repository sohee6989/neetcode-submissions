class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            print(stones)
            first_large_num = stones.pop()
            second_large_num = stones.pop()
            print(first_large_num)
            print(second_large_num)
            if first_large_num > second_large_num:
                new_num = first_large_num - second_large_num
                stones.append(new_num)
        
        if stones:
            return stones[0]
        else:
            return 0