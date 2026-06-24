class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversedNumber = 0
        number = x

        while number > 0:
           reversedNumber = (number % 10) + (reversedNumber * 10)
           number //= 10
        
        return x == reversedNumber