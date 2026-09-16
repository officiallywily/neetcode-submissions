class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return
        stack: List[str] = []
        while len(tokens) > 0:
            stack.append(tokens.pop())
            
        operators: Set[str] = {"+", "-", "*", "/"}
        operands = []
        while len(stack) > 0:
            popped = stack.pop()
            if popped in operators:
                operand2 = operands.pop()
                operand1 = operands.pop()
                if popped == "+":
                    operands.append(operand1 + operand2)
                elif popped == "-":
                    operands.append(operand1 - operand2)
                elif popped == "*":
                    operands.append(operand1 * operand2)
                elif popped == "/":
                    operands.append(int(operand1 / operand2))
            else:
                operands.append(int(popped))

        return operands.pop()
