class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        leftHalf = self.sortArray(nums[:mid])
        rightHalf = self.sortArray(nums[mid:])

        return self.merge(leftHalf, rightHalf)

    def merge(self, left, right):
        sortedArray = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sortedArray.append(left[i])
                i += 1
            else:
                sortedArray.append(right[j])
                j += 1
        
        while i < len(left):
            sortedArray.append(left[i])
            i += 1

        while j < len(right):
            sortedArray.append(right[j])
            j += 1
        
        return sortedArray


        