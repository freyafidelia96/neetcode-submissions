class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstStr = strs[0]
        res = ""

        for i in range(len(firstStr)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or firstStr[i] != strs[j][i]:
                    return res
       
            res += firstStr[i]


        return res
        