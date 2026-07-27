class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            num_hash = {str(i): 0 for i in range(1, 10)}
            num_hash2 = {str(i): 0 for i in range(1, 10)}

            for j in range(9):
                if board[i][j] in num_hash:
                    num_hash[board[i][j]] += 1

                    if num_hash[board[i][j]] >= 2:
                        return False 

                if board[j][i] in num_hash:
                    num_hash2[board[j][i]] += 1

                    if num_hash2[board[j][i]] >= 2:
                        return False 
                
        
        for i in range(3):
            num_hash3 = {str(i): 0 for i in range(1, 10)}
            print("num_hash3", num_hash3)

            for j in range(3):
                num_hash3 = {str(i): 0 for i in range(1, 10)}
                for k in range(3):
                    print("1", i*3, j*3+k, board[i * 3][j * 3 + k])
                    if board[i * 3][j * 3 + k] in num_hash3:
                        # print("1 출력")
                        num_hash3[board[i * 3][j * 3 + k]] += 1

                        if num_hash3[board[i * 3][j * 3 + k]] >= 2:
                            return False 

                for k in range(3):
                    print("2", i*3+1, j*3+k, board[i * 3 + 1][j * 3 + k])
                    if board[i * 3 + 1][j * 3 + k] in num_hash3:
                    # print(i*3+1, i*3+j, board[i * 3 + 1][i * 3 + j])
                        # print("2 출력")
                        num_hash3[board[i * 3 + 1][j * 3 + k]] += 1

                        if num_hash3[board[i * 3 + 1][j * 3 + k]] >= 2:
                            return False 

                for k in range(3):
                    print("3", i * 3 + 2, i * 3 + k, board[i * 3 + 2][j * 3 + k])
                    if board[i * 3 + 2][j * 3 + k] in num_hash3:
                        # print("3 출력")
                        num_hash3[board[i * 3 + 2][j * 3 + k]] += 1

                        if num_hash3[board[i * 3 + 2][j * 3 + k]] >= 2:
                            return False 

                print(num_hash3)
        return True

        