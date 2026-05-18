class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        index = -1
        for i, num in enumerate(nums):

            if num == val:
                while index > -len(nums) and nums[index] == val:
                    index -= 1
                if index > -len(nums):
                    nums[i] = nums[index]
                    index -= 1
            else:
                k += 1

        return k
            
        