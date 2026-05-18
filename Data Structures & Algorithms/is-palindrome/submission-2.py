class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newS = s.split(" ")
        # newS = "".join(newS)

        # count = len(newS) // 2
        # index = -1

        # for i in range(count):
        #     if ord(newS[index]) < 65 or ord(newS[index]) > 122:
        #         index -= 1
        #     if newS[i].lower() != newS[index].lower():
        #         return False
        #     index -= 1
        # return True

        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
