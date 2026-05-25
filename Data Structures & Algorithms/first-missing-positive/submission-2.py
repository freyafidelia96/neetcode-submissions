class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # n = 1

        # for num in nums:
        #     if num == n:
        #         n += 1
        
        # return n
        
        # numsSet = set(nums)

        # for i in range(1, len(numsSet) + 1):
        #     if i not in numsSet:
        #         return i
        
        # return len(numsSet) + 1

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
