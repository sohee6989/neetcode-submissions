class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                estimated_ch = ''
                if ch == ')':
                    estimated_ch = '('
                elif ch == ']':
                    estimated_ch = '['
                elif ch == '}':
                    estimated_ch = '{'
                
                if not stack or estimated_ch != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True
        