class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # n = 1

        # for num in nums:
        #     if num == n:
        #         n += 1
        
        # return n
        
        numsSet = set(nums)

        for i in range(1, len(numsSet) + 1):
            if i not in numsSet:
                return i
        
        return len(numsSet) + 1
