class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if bracket == ')':
                    if stack != []:
                        if stack.pop() != '(':
                            return False
                    else:
                        return False
                elif bracket == '}':
                    if stack != []:
                        if stack.pop() != '{':
                            return False
                    else:
                        return False
                elif bracket == ']':
                    if stack != []:
                        if stack.pop() != '[':
                            return False
                    else:
                        return False

        return stack == []

        