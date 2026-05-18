from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = Counter(nums)

        for num in nums:
            if numsCount[num] > 1:
                return True

        return False

         