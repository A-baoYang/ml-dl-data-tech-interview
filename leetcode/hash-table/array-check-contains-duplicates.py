from design_hash_set import CustomHashSet


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = CustomHashSet(10 ** 6)
        for k in nums:
            hashset.add(k)
            if hashset.contains(k):
                return True
        return False
