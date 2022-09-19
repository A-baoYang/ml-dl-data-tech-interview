# (1)
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict(Counter(list(s)))
        counter = {k: v for k, v in counter.items() if v == 1}
        if not counter:
            return -1
        else:
            p = list(counter.keys())[0]
            return s.index(p)


# (2)
# 执行用时：88 ms 在所有 Python3 提交中击败了 74.13% 的用户
# 内存消耗：15 MB 在所有 Python3 提交中击败了 95.89% 的用户
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counter = dict(Counter(list(s)))
        # counter = {k: v for k, v in counter.items() if v == 1}
        # if not counter:
        #     return -1
        # else:
        #     p = list(counter.keys())[0]
        #     return s.index(p)
        unique, repeat = list(), set()
        for c in s:
            if c not in unique and c not in repeat:
                unique.append(c)
            elif c in unique:
                unique.remove(c)
                repeat.add(c)
        if not unique:
            return -1
        return s.index(unique[0])
