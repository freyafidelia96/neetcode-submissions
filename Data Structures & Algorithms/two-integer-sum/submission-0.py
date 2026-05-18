class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}

        result = []
        
        for i in range(len(nums)):
            if target - nums[i] in numsDict:
                result += [numsDict[target - nums[i]], i]
            else:
                numsDict[nums[i]] = i

        return result
