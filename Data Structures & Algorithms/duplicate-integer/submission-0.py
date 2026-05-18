class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lengthOfNums = len(nums)
        numsAsSet = set(nums)
        lengthOfnumsAsSet = len(numsAsSet)

        return lengthOfNums > lengthOfnumsAsSet


         