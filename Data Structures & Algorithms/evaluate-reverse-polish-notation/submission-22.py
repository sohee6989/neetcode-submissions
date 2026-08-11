class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_array = []

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            # print("token", token)
            # print("num_array", num_array)
            if token.isdigit():
                # print("여기 출력")
                token = int(token)
                num_array.append(token)
            elif token.startswith('-') and token[1:].isdigit():
                num_array.append(-int(token[1:]))
            else:
                second_num = num_array.pop()
                first_num = num_array.pop()
                # print("first_num", first_num)
                # print("second_num", second_num)
                result = calculate(first_num, second_num, token)
                num_array.append(result)
                # print("num2", num_array)
        
        return result
    
def calculate(num1: int, num2: int, op: str):
    result = 0

    if op == '+':
        result = num1 + num2
    elif op == '*':
        result = num1 * num2
    elif op == '-':
        result = num1 - num2
    else:
        result = int(num1 / num2)
        
    return result