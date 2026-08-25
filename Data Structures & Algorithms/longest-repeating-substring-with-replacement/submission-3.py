class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characterCount = [0] * 26
        l = 0
        res = 0

        for r in range(len(s)):
            characterCount[ord(s[r]) - ord('A')] += 1
            maxFreq = max(characterCount)

            while (r - l) + 1 - maxFreq > k:
                characterCount[ord(s[l]) - ord('A')] -= 1
                l += 1
                
            res = max(res, r-l+1)

        return res
            

