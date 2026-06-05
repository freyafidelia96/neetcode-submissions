class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "D":
                lastInteger = stack[-1]
                stack.append(2 * lastInteger)
            elif op == "C":
                stack.pop()
            elif op == "+":
                secondOperand = stack[-1]
                firstOperand = stack[-2]
                stack.append(firstOperand + secondOperand)
            else:
                stack.append(int(op))

        return sum(stack)
        