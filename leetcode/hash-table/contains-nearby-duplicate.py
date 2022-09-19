# (1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist = {}
        for i, n in enumerate(nums):
            if n not in dist:
                dist.update({n: i})
            else:
                if i - dist[n] <= k:
                    return True
                else:
                    dist[n] = i
        return False


# (2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            if abs(i - dist[n]) and abs(i - dist[n]) <= k:
                return True
            else:
                dist[n] = i
        return False
