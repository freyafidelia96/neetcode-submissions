class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxSoFar = 0
        # for i, a in enumerate(heights):
        #     for j in range(i+1, len(heights)):
        #         area = min(a, heights[j]) * (j - i)
        #         maxSoFar = max(area, maxSoFar)

        # return maxSoFar

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return res


        