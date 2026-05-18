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
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res



