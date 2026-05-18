class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstStr = strs[0]
        res = ""
        isChecking = True

        for i in range(len(firstStr)):
            for j in range(1, len(strs)):
                try:
                    if firstStr[i] != strs[j][i]:
                        isChecking = False
                except Exception as e:
                    isChecking = False
                    print(e)

            if not isChecking:
                break

            res += firstStr[i]


        return res
        