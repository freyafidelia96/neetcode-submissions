class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{"}

        # for bracket in s:
        #     if bracket == '(' or bracket == '{' or bracket == '[':
        #         stack.append(bracket)
        #     else:
        #         if bracket == ')':
        #             if stack != []:
        #                 if stack.pop() != '(':
        #                     return False
        #             else:
        #                 return False
        #         elif bracket == '}':
        #             if stack != []:
        #                 if stack.pop() != '{':
        #                     return False
        #             else:
        #                 return False
        #         elif bracket == ']':
        #             if stack != []:
        #                 if stack.pop() != '[':
        #                     return False
        #             else:
        #                 return False

        # return stack == []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        