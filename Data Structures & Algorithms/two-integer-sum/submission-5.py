class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in checked:
                return [checked[comp], i]
            checked[nums[i]] = i