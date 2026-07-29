class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        isStart = False
        isEnd = False

        if isPossible(start, h, piles) :
            isStart = True
        else:
            isStart = False
            
        if isPossible(end, h, piles):
            isEnd = True
        else:
            isEnd = False

        if isStart:
            return start

        while start < end:
            
            if end - start == 1:
                return end
        
            half_index = start + (end - start) // 2

            isHalf = isPossible(half_index, h, piles)

            if not (isHalf ^ isStart):
                start = half_index
            else:
                end = half_index
        

    
def isPossible(rate: int, h: int, piles: List[int]) -> bool:
    hours = 0

    for p in piles:
        if (p % rate == 0):
            hours += p // rate
        else:
            hours += (p // rate + 1)
        
    if hours <= h:
        return True
    else:
        return False

        