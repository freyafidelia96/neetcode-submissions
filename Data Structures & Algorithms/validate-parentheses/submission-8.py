class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkToOpen = { ')': '(', ']':'[', '}':'{' }

        for c in s:
            if c in checkToOpen:
                if stack and checkToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
                
        



"""
s = (({[]}))
read s[0]
push to stack
read s[1] and s[2] and s[3]
push to stack
read s[4] and see it is a closing tag so we want to check the stack for the equivalent opening tag
if it is not immediately return false
if it is remove it from the stack

"""