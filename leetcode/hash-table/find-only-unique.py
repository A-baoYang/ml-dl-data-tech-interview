#### (1)

from design_hash_set import CustomHashSet


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = CustomHashSet(10 ** 6)
        single_nums = []
        for k in nums:
            if hashset.contains(k):
                single_nums.remove(k)
            else:
                hashset.add(k)
                single_nums.append(k)
        return single_nums[0]


#### (2)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for k in nums:
            if k in hashset:
                hashset.remove(k)
            else:
                hashset.add(k)
        for k in hashset:
            return k
