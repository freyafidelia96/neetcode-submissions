class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while top < bottom and target > matrix[top][right - 1]:
            top += 1

        if top < bottom:
            for i in range(left, right):
                if matrix[top][i] == target:
                    return True
    
        return False