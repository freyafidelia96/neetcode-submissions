import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNumbers = {}
        x = math.floor(len(nums) / 2)

        for i, n in enumerate(nums):
                if n in countNumbers:
                    countNumbers[n] += 1
                else:
                    countNumbers[n] = 1

        for key, value in countNumbers.items():
             if value > x:
                return key
        