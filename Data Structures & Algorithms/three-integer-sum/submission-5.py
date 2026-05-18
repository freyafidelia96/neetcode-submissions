class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        # nums.sort()
        # lenN = len(nums)

        # for i in range(lenN):
        #     for j in range(i + 1, lenN):
        #         for k in range(j + 1, lenN):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp))

        # return [list(i) for i in res]
        # from collections import Counter
        # res = []
        # nums.sort()
        # countNums = Counter(nums)
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res



