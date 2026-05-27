class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()

        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
            
        #     res = max(res, len(charSet))
        # return res
        
        left = res = 0
        checked = set()

        for right in range(len(s)):
            while s[right] in checked:
                checked.remove(s[left])
                left += 1
            checked.add(s[right])
            res = max(res, right - left + 1)
        
        return res
