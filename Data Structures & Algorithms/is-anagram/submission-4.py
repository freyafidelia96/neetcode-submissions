class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_chars = sorted(s)
        sorted_s = "".join(sorted_chars)

        sorted_chars = sorted(t)
        sorted_t = "".join(sorted_chars)

        if sorted_s == sorted_t:
            return True
        else:
            return False

