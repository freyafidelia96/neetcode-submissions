class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in checked:
                return [checked[x], i]
            
            checked[nums[i]] = i 
        