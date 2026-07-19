class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []

        for i in range(len(temperatures)):
            day = 0
            for j in range(i + 1, len(temperatures)):
                day += 1
                if temperatures[j] > temperatures[i]:
                    output.append(day)
                    break
                
                if j == len(temperatures) - 1:
                    output.append(0)
            
            if i == len(temperatures) - 1:
                output.append(0)
            
        return output
