class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        
        for token in tokens:
            if token.lstrip('-').isdigit():  # Correctly identify numbers, including negatives
                operand_stack.append(int(token))
            else:
                # Pop the last two operands from the stack for the operation
                b = operand_stack.pop()
                a = operand_stack.pop()
                
                # Perform the appropriate operation
                if token == "+":
                    operand_stack.append(a + b)
                elif token == "-":
                    operand_stack.append(a - b)
                elif token == "*":
                    operand_stack.append(a * b)
                elif token == "/":
                    # Perform integer division that truncates toward zero
                    operand_stack.append(int(a / b))
        
        return operand_stack[0]







        