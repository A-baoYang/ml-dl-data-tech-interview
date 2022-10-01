class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for c in [i, i+1]:
                _ = self.matcher(s, i, c)
                if len(_) > len(res):
                    res = _
        return res

    def matcher(self, s:str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
