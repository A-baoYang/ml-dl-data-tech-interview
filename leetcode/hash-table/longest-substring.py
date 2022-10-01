def lengthOfLongestSubstring(s: str) -> int:
    dct, res, prev = {}, 0, -1
    for i, v in enumerate(s):
        if v in dct and prev < dct[v]:
            n = i - dct[v]
            prev = dct[v]
        else:
            n = i - prev
        res = n if n > res else res
        dct[v] = i
    return res
