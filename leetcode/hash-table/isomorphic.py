class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_unique, t_unique = {}, {}
        for idx, _ in enumerate(s):
            if s[idx] not in s_unique:
                s_unique[s[idx]] = idx
            if t[idx] not in t_unique:
                t_unique[t[idx]] = idx
            if s_unique[s[idx]] != t_unique[t[idx]]:
                return False
        return True
