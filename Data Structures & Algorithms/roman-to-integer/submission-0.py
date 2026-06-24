class Solution:
    def romanToInt(self, s: str) -> int:
        l = 0
        r = 1

        romanNumeralsDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        while r < len(s):
            if romanNumeralsDict[s[l]] < romanNumeralsDict[s[r]]:
                res += romanNumeralsDict[s[r]] - romanNumeralsDict[s[l]]
                l = r + 1
                r = r + 2
            else:
                res += romanNumeralsDict[s[l]]
                l += 1
                r += 1


        while l < len(s):
            res += romanNumeralsDict[s[l]]
            l += 1

        return res
        