class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        count = {
            k: v for k, v in sorted(count.items(), key=lambda x: x[1], reverse=True)
        }
        return list(count.keys())[:k]
