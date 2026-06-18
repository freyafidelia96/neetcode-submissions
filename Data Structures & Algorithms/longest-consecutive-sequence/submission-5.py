class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        setNums = set(nums)

        for num in setNums:
           if num - 1 not in setNums:
            currCount = 1

            while num + currCount in setNums:
                currCount += 1
            
            maxCount = max(currCount, maxCount)

        return maxCount

            
        