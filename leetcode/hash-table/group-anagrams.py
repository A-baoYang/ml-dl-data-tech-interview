class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in groups:
                groups[ss] = [s]
            else:
                groups[ss].append(s)
        return list(groups.values())
