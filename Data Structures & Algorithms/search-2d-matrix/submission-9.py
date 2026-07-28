class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = [0, 0]
        end = [0, n - 1]

        if m == 1 and n == 1:
            if matrix[0][0] != target:
                return False
            else:
                return True
        
        for i in range(m - 1 , 0, -1):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                start[0] = i
                end[0] = i
                break

        while True:
            half_index = start[1] + (end[1] - start[1]) // 2
            if n == 1:
                if matrix[start[0]][start[1]] == target:
                    return True
                else:
                    return False

            if matrix[start[0]][start[1]] == target:
                return True
            
            if matrix[end[0]][end[1]] == target:
                return True
            
            if end[1] - start[1] == 1:
                return False
            
            if matrix[start[0]][half_index] < target:
                start[1] = half_index
            elif matrix[start[0]][half_index] > target:
                end[1] = half_index
            else:
                return True

        return False