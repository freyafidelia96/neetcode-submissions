class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = []

        for row in range(numRows):
            increment = (numRows - 1) * 2

            for column in range(row, len(s), increment):
                res.append(s[column])
                if row > 0 and row < numRows - 1 and column + increment - 2 * row < len(s):
                    res.append(s[column + increment - 2 * row])

        return ''.join(res)