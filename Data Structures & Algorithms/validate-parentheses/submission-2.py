class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map opening brackets to their corresponding closing brackets
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        # Stack to keep track of opening brackets
        stack = []
        
        for char in s:
            if char in bracket_dict:
                # If it's an opening bracket, push to stack
                stack.append(char)
            else:
                # If it's a closing bracket, check for a match
                if not stack or bracket_dict[stack.pop()] != char:
                    return False
        
        # If stack is empty, all brackets matched correctly
        return len(stack) == 0