class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_array = []

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            # digit은 음수 기호(-)나 소수점(.)이 있으면 False를 반환
            if token.isdigit(): 
                token = int(token)
                num_array.append(token)
            elif token.startswith('-') and token[1:].isdigit():
                num_array.append(-int(token[1:]))
            else:
                second_num = num_array.pop()
                first_num = num_array.pop()
                result = self.calculate(first_num, second_num, token)
                num_array.append(result)
        
        return result
    
    def calculate(self, num1: int, num2: int, op: str):
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